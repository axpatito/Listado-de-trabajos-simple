import json
from orm import Model

class Trabajo(Model):

    id_alumno = int
    nombre_alumno = str
    nombre_trabajo = str
    paginas_trabajo = int
    fecha = str
    hora = float

    def __init__(self, *args, **kwargs):
        self.id_alumno = kwargs['id_alumno']
        self.nombre_alumno = kwargs['nombre_alumno']
        self.nombre_trabajo = kwargs['nombre_trabajo']
        self.paginas_trabajo = kwargs['paginas_trabajo']
        self.fecha = kwargs['fecha']
        self.hora = kwargs['hora']

    def export_json(self):
        return json.dumps(self.__dict__)

    def get_formated_keys(self):
        return self.__dict__.keys()
