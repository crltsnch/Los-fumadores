from fumador import *

class Agente:
    def dejar_ingredientes(self, ingredientes):
        print('Agente inciiado')
        while True:
            #Elegir dos ingredientes al azar
            ing1, ing2 = random.sample(['papel', 'tabaco', 'filtros', 'green', 'mechero'], 2)
            #Agregar los ingredientes a la lista de ingredientes disponibles
            ingredientes.extend([ing1, ing2])
            #Esperar a que un fumador termine
            tarea_completada = app.tasks['agente.tarea_completada']
            tarea_completada.apply_async().get()
            print(f'Fumador ha terminado, nueva ronda...')
            time.sleep(1)
            