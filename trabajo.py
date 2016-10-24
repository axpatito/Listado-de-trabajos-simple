import json
from orm import Model
import consts
import collections
import copy

class Trabajo(Model):

    id_alumno = int
    nombre_alumno = str
    nombre_trabajo = str
    paginas_trabajo = int
    fecha = str
    hora = float

    def __init__(self, *args, **kwargs):
        self.id_alumno = 3,
        if isinstance(self.id_alumno, tuple):
            self.id_alumno = self.id_alumno[0]
        self.nombre_alumno = kwargs['nombre_alumno']
        self.nombre_trabajo = kwargs['nombre_trabajo']
        self.paginas_trabajo = int(kwargs['paginas_trabajo'])
        self.fecha = kwargs['fecha']
        self.hora = kwargs['hora']

    def get_ordered_dict(self):
        return collections.OrderedDict(sorted(self.get_filetered_dict().items()))

    def get_ordered_keys(self):
        return sorted(self.get_ordered_dict().keys())

    def get_filetered_dict(self):
        return {key: val for key, val in self.__dict__.iteritems()
                if key != consts.ID and key != consts.ID_ALUMNO}
