from datetime import datetime
from sqlite3 import Date
import string
import json

class Evento:

    codigo :int
    nombre :string
    numEntradas :int
    fecha : datetime

    def __init__(self,codigo,nombre,numEntradas,fecha):
        self.codigo = codigo
        self.nombre = nombre
        self.numEntradas = numEntradas
        fechaAux = fecha.split('-')
        self.fecha = datetime(int(fechaAux[2]),int(fechaAux[1]),int(fechaAux[0]))





    


