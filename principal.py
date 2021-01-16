import requests
import config

una_lista = [1,2,3,4,5,6,7]

for elemento in una_lista:
    print("Hola Elemento N°", elemento)

nombres = ["Guido", "Fernando", "Rocío", "Francisca", "Nicolás", "Miguel", "Luis"]

for alumno in nombres:
    print("Hola Alumno:", alumno)

for variable, valor in vars(config).items():
    print(variable, valor)
