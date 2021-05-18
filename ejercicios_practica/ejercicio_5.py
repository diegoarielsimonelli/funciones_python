# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones y módulos
import random

# --------------------------------
# Aquí dentro definir la función contar

def contar(lista_numeros):
    
    for i in range(lista_numeros,3):    
        cantidad_tres = lista_numeros.count(3) 
        print (cantidad_tres)
# Aquí copiar la función lista_aleatoria
# ya elaborada
def lista_aleatoria(inicio, fin, cantidad):
    
    mi_lista_aleatoria=[]
    for i in range(cantidad):
        numero = random.randrange(inicio, fin+1)
        mi_lista_aleatoria.append(numero)
        print("lista aleatoria:",mi_lista_aleatoria)

# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    inicio = 0
    fin = 9
    cantidad = 5

    # Alumno: Crear la función "contar"
    numero = random.randrange(inicio, fin+1)
 
    # Utilice la función "lista_aleatoria"  creado antes 
    # para generar una lista de 5 números en
    # un rango de 1 a 9 inclusive
    lista_numeros = lista_aleatoria(inicio, fin, cantidad)
    # lista_numeros = lista_aleatoria(inicio, fin, cantidad)

    # Generar una una nueva funcion que se llame "contar",
    #que cuenta la cantidad de veces que un elemento pasado
    # por parámetro se repite en la lista también pasada por parámetro
    
    # Para saber cuantas veces se repiten el elemento pasado
    # en la lista pueden usar el método nativo de list "count"

    # Por ejemplo creo una lista de 5 elemtnos
    mi_lista_aleatoria= lista_aleatoria(inicio, fin, cantidad)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    cantidad_tres = contar(lista_numeros,3)

    # Luego de crear la función invocarla en este lugar:
    # Averiguar cuantas veces se repite el numero 3
    #cantidad_tres = contar(lista_numeros, 3)

    # cantidad_tres = contar(lista_numeros, 3)

    # Imprimir en pantalla "cantidad_tres" que informa
    # cuantas veces se repite el tres en la lista

    # print(cantidad_tres)
    print(cantidad_tres)

    print("terminamos")