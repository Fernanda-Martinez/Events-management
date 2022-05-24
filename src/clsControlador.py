from datetime import datetime
from .clsEvento import Evento
from .clsConexion import Conexion
import json

class Controlador:

    listaEventos: Evento  = []   
  
    def obtenerDatos(self):
        self.listaEventos = []
        jsonLista = Conexion.iniciarBase()
        for json in jsonLista:
            cod = json[0]
            nombre = json[1]
            numEntradas = json[2]
            fecha = json[3]
            evento = Evento(cod,nombre,numEntradas,fecha)
            
            self.listaEventos.append(evento)


    def buscarCodigo (self, cod):
        for event in self.listaEventos:
            if event.codigo == cod :
                return event

        print("No existe un evento con ese código D:")    
                

    def buscarNombre (self, nom):
        for event in self.listaEventos:
            if event.nombre == nom :
                return event
            
        print("No existe un evento con ese nombre :(")

    def mostrar(self):
        for event in self.listaEventos:
            print("------------------------------------------------------------------------------------")
            print("Código: ", event.codigo)
            print("Nombre: ", event.nombre)
            print("Número de entradas disponibles: ", event.numEntradas)
            print("Fecha del evento: ", event.fecha)

    def comprarEntrada(self, cod, entradas):
        bc = self.buscarCodigo(cod)
        fechaAct = datetime.today()
        if bc.numEntradas > 0 or bc.numEntradas - entradas < 0:
            if fechaAct < bc.fecha :
               Conexion.actualizarEntradas(bc,bc.numEntradas - entradas)
               self.obtenerDatos()
            else:
                print("Lo sentimos, no fue posible comprar las entradas debido a que este evento ya está muy próximo o ya pasó")
        else:
            print("Lo sentimos, No hay suficientes entradas para este evento")

    def crearEvento(self,cod, nombre, numEntradas, fecha):
        evento =Evento(cod,nombre,numEntradas,fecha) 
        Conexion.insertarDatos(evento)
        self.obtenerDatos()

        
        






