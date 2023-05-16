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

                #Terminar 