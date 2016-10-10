import json
from orm import Model

class Trabajo(Model):

    id_alumno = int
    nombre_alumno = str
    nombre_trabajo = str
    paginas_trabajo = int
    fecha = str
    hora = float

    def __init__(self, id_alumno, nombre_alumno, nombre_trabajo, paginas_trabajo, fecha, hora):
        self.id_alumno = id_alumno
        self.nombre_alumno = nombre_alumno
        self.nombre_trabajo = nombre_trabajo
        self.paginas_trabajo = paginas_trabajo
        self.fecha = fecha
        self.hora = hora

    def export_json(self):
        return json.dumps(self.__dict__)

    def get_formated_keys(self):
        return self.__dict__.keys()
