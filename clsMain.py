##Angie Carolina Gómez-Maria Fernanda Martínez-Juan Esteban Ruiz
from src.clsControlador import Controlador

class Main:
    controlador = Controlador()
    controlador.obtenerDatos()
    while 1:
        print()
        print("1. Agregar los datos de un evento")
        print("2. Buscar un evento por código")
        print("3. Buscar un evento por nombre")
        print("4. Mostrar todos los eventos")
        print("5. Comprar entradas")
        print("6. Salir")
        print()
        op = int(input("Digite una opción: "))
        print()

        if op == 1:
            cod = int(input("Digite el codigo del evento a crear: "))
            nombre = (input("Digite el nombre del evento a crear: "))
            numEntradas = int(input("Digite el número de entradas del evento a crear: "))
            fecha = (input("Digite la fecha del evento a crear, en el siguiente formato DD-MM-YYYY: "))
            controlador.crearEvento(cod,nombre,numEntradas,fecha)

        if op == 2:
            evento = controlador.buscarCodigo(int(input("Digite el codigo del evento a buscar: ")))
            print("------------------------------------------------------------------------------------")
            print('Código: ', evento.codigo)
            print('Nombre del evento: ', evento.nombre)
            print('Número de Entradas: ', evento.numEntradas)
            print('Fecha del evento: ', evento.fecha)


        if op == 3:
            evento = controlador.buscarNombre(input("Digite el nombre del evento a buscar: "))
            print("------------------------------------------------------------------------------------")
            print('Código: ', evento.codigo)
            print('Nombre del evento: ', evento.nombre)
            print('Número de Entradas: ', evento.numEntradas)
            print('Fecha del evento: ', evento.fecha)

        
        if op == 4:
            controlador.mostrar()

        if op == 5:
            controlador.comprarEntrada(int(input("Digite el codigo del evento al que va a comprar entradas: ")), int(input("Digite el numero de entradas a comprar: ")))

        if op == 6:
            print("El programa finalizó")
            exit()


    

