from trabajo import Trabajo
import consts
from orm import Database
from flask import Flask, render_template, request, url_for
import random
import logging
import copy
# logger = logging.getLogger('stats_server')
# logging.basicConfig(filename=consts.LOG_FILE, level=logging.DEBUG)

app = Flask(__name__)
db = Database(consts.DB)
Trabajo.db = db

@app.route('/')
def index():
    trabajos = list(Trabajo.manager(db).all())
    return render_template('listado.html', trabajos=trabajos, cabeceras=trabajos[0].__dict__.keys())


@app.route('/api/crear_trabajo', methods=['POST'])
def crear_trabajo():
    post_values = request.values.to_dict()
    mi_trabajo = Trabajo(**post_values)
    try:
        mi_trabajo.save()
        db.commit()
        return 'Ok'
    except Exception as e:
        import ipdb; ipdb.set_trace()
        return e, 500

@app.route('/crea_ejemplo')
def create_db_example():
    nombre_alumnos = ['javier', 'gabriel', 'rodrigo']
    nombre_trabajo = ['quimica', 'fisica', 'matematicas']
    trabajo_dict = copy.deepcopy(consts.TRABAJO_DICT)
    trabajo_dict['id_alumno'] = random.randint(200, 500)
    trabajo_dict['nombre_alumno'] = random.choice(nombre_alumnos)
    trabajo_dict['nombre_trabajo'] = random.choice(nombre_trabajo)
    trabajo_dict['paginas_trabajo'] = 2
    trabajo_dict['fecha'] = '2016-01-01'
    trabajo_dict['hora'] = 12
    mi_trabajo = Trabajo(**trabajo_dict)
    try:
        mi_trabajo.save()
        db.commit()
        return 'Ok'
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run(port=consts.PORT)
