from trabajo import Trabajo
import consts
from orm import Database
from flask import Flask, render_template, request, url_for
import random
import logging
logger = logging.getLogger('stats_server')
logging.basicConfig(filename=consts.LOG_FILE, level=logging.DEBUG)

app = Flask(__name__)
db = Database(consts.DB)
Trabajo.db = db

@app.route('/')
def index():
    trabajos = list(Trabajo.manager(db).all())
    return render_template('listado.html', trabajos=trabajos, cabeceras=trabajos[0].__dict__.keys())


@app.route('/api/crear_trabajo', methods=['POST'])
def crear_trabajo():
    return None

@app.route('/crea_ejemplo')
def create_db_example():
    nombre_alumnos = ['javier', 'gabriel', 'rodrigo']
    nombre_trabajo = ['quimica', 'fisica', 'matematicas']
    mi_trabajo = Trabajo(
        id_alumno=random.randint(200,500),
        nombre_alumno=random.choice(nombre_alumnos),
        nombre_trabajo=random.choice(nombre_trabajo),
        paginas_trabajo=2,
        fecha='2016-01-01',
        hora=12,
    )
    try:
        mi_trabajo.save()
        db.commit()
        return 'Ok'
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run(port=consts.PORT)