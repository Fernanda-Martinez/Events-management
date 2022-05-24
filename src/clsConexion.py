from ast import Try
from .clsEvento import Evento
import sqlite3


class Conexion:

    def iniciarBase():
        try:
            conexion = sqlite3.connect('eventosDB.db')
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM evento')
            info = cursor.fetchall()
            return info
        except Exception as e:
            print(e)

       

    def insertarDatos(evento : Evento):
        try:     
            conexion = sqlite3.connect('eventosDB.db')
            cursor = conexion.cursor()
            eventoFecha = evento.fecha
            fechaActu = eventoFecha.strftime('%d-%m-%Y')
            cursor.execute('INSERT INTO evento (codigo, nombre, numEntradas, fecha) VALUES (?,?,?,?)',(evento.codigo,evento.nombre, evento.numEntradas,fechaActu))
            conexion.commit()
            print("El evento se creó correctamente")
               
        except Exception as e:
            print(e)

    def actualizarEntradas(evento : Evento, numEntradas):
        try:
            conexion = sqlite3.connect('eventosDB.db')
            cursor = conexion.cursor()
            cursor.execute('UPDATE evento SET numEntradas =? WHERE codigo = ?',(numEntradas,evento.codigo))
            conexion.commit()
            print("La compra de entradas al evento fue exitosa ")
        except Exception as e:
            print(e)