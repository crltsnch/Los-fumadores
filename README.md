# Los-fumadores

El link a mi repositorio es: [GitHub](https://github.com/crltsnch/Los-fumadores)

#Archivo `fumador.py`

```
import time
import random
from celery import Celery

app = Celery('fumador', broker = 'pyamqp://guest@localhost//')

#Definicon de la clase fumador
class Fumador:
    def __init__(self, id, ing1, ing2, ingredientes):
        self.id = id
        self.ing1 = ing1
        self.ing2 = ing2
        self.ingredientes = ingredientes
    
    def fumar(self):
        print(f'Fumador {self.id} esperando por {self.ing1} y {self.ing2}')
        while True:
            #Esperar hasta qu eambos ingredientes estén disponibles
            if self.ing1 in self.ingredientes and self.ing2 in self.ingredientes:

                #Tomar los ingredientes
                self.ingredientes.remove(self.ing1)
                self.ingredientes.remove(self.ing2)
                print(f'Fumador {self.id} tomando {self.ing1} y {self.ing2} y fumando')
                time.sleep(random.randint(1, 3))

                #Agregar los ingredientes usados nuevamente a la lista de inredientes
                self.ingredientes.append(self.ing1)
                self.ingredientes.append(self.ing2)

                #Publicar un mensaje para indicar que el fumador ha terminado
                app.send_task('agente.tarea_terminada', args = [self.id])
                break
```

#Archivo `agente.py`

```
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
        
```

#Archvio `main.py`

```
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
    fumador1.fumar()
    fumador2.fumar()
    fumador3.fumar()

    #Crear instancias del agente
    agente = Agente()

    #Iniicar la tarea del agente
    agente.dejar_ingredientes.delay(ingredientes)

if __name__ == '__main__':
    main()
    
```    
