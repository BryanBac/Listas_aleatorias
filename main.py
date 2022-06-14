import random
from typing import List
import pywhatkit as rep


lista_bryan: List = ["https://youtu.be/XMeQeIG_rQg",
                     "https://youtu.be/T4y7imuU4nM",
                     "https://youtu.be/QEAHvpXtE2s",
                     "https://youtu.be/ShEAiFqkY0E",
                     "https://youtu.be/1PSLSsU08Mk",
                     "https://youtu.be/HrE6LjIwK84",
                     "https://youtu.be/GhGTc6p8sg0",
                     "https://youtu.be/9jvVBVcZ0-Y",
                     "https://youtu.be/BHncfQjJb_w",
                     "https://youtu.be/6CBp4qylX6I"]
lista_ale: List = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
opcion: int = 0
cantidad_de_vueltas: int = 9
while opcion != 2:
    print("######## Menu ########")
    print("1. Aleatorio")
    print("2. Salir")
    opcion = int(input("Elija su opcion: "))
    if opcion == 1:
        aleatorio_bryan: int = random.randint(0, cantidad_de_vueltas)
        aleatorio_ale: int = random.randint(0, cantidad_de_vueltas)
        cantidad_de_vueltas -= 1
        opcion2: int = 0
        while opcion2 != 3:
            print("1. Reproducir Bryan")
            print("2. Reproducir Ale")
            print("3. Regresar al menu inicial")
            opcion2 = int(input("Teclee"))
            if opcion2 == 1:
                rep.playonyt(lista_bryan[aleatorio_bryan])
                lista_bryan.pop(aleatorio_bryan)
            if opcion2 == 2:
                rep.playonyt(lista_ale[aleatorio_ale])
                lista_ale.pop(aleatorio_ale)
