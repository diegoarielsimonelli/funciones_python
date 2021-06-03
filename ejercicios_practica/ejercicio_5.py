import random

def tirar():
    dados=[]
    for i in range(5):
        dados.append(random.randint(1,6))
    return dados
dados=tirar()
print(dados)
def contar(tirar, numero):
    
    cantidad_tres = tirar.count(numero) 
    print (cantidad_tres)
    return cantidad_tres
    
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    cantidad_tres= contar(dados, 3)

    # Alumno: Crear la función "contar"
    
 
    # Utilice la función "lista_aleatoria"  creado antes 
    # para generar una lista de 5 números en
    # un rango de 1 a 9 inclusive
    
   
    # lista_numeros = lista_aleatoria(inicio, fin, cantidad)

    # Generar una una nueva funcion que se llame "contar",
    #que cuenta la cantidad de veces que un elemento pasado
    # por parámetro se repite en la lista también pasada por parámetro
    
    # Para saber cuantas veces se repiten el elemento pasado
    # en la lista pueden usar el método nativo de list "count"

    # Por ejemplo creo una lista de 5 elemtnos
    
    # Luego quiero averiguar cuantas veces se repite el numero 3
    

    # Luego de crear la función invocarla en este lugar:
    # Averiguar cuantas veces se repite el numero 3
    #cantidad_tres = contar(lista_numeros, 3)

    # cantidad_tres = contar(lista_numeros, 3)

    # Imprimir en pantalla "cantidad_tres" que informa
    # cuantas veces se repite el tres en la lista

    # print(cantidad_tres)


    print("terminamos")