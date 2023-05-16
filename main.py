from agente import *
from fumador import *

def main():
    #Lista de ingredientes disponibles en la mesa
    ingredientes = []

    #Crear instancias de los fumadores
    fumador1 = Fumador(1, 'papel', 'tabaco', ingredientes)
    fumador2 = Fumador(2, 'tabaco', 'filtros', ingredientes)
    fumador3 = Fumador(3, 'papel', 'filtros', ingredientes)

    #Iniciar las tareas de los fuamdores
    fumador1.fumar.delay()
    fumador2.fumar.delay()
    fumador3.fumar.delay()

    #Crear instancias del agente
    agente = Agente()

    #Iniicar la tarea del agente
    agente.dejar_ingredientes.delay(ingredientes)

if __name__ == '__main__':
    main()