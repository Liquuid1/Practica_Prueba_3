import os

def mostrar_menu():
    menu = """[1] Agregar pelicula
[2] Listar peliculas
[3] Buscar pelicula
[4] Salir
--> """
    print(menu,end="")
    
def get_opcion():
    while True:
        try:
            op = int(input())

            if op>=1 and op<=4:
                return op
            else:
                raise ValueError
        except:
            print("Ingresa una opcion valida --> ",end="")

def agregar_pelicula():
    cod = input("Ingresa el codigo de la pelicula: ")
    nombre = input("Ingresa el nombre de la pelicula: ")
    categoria = input("Ingresa la categoria de la pelicula: ")
    director = input("Ingresa el director de la pelicula: ")
    anio = input("Ingresa el año de la pelicula: ")

    res = {"codigo":cod,"nombre":nombre,"categoria":categoria,"director":director,"año":anio}
    return res

def listar_peliculas(lista):
    for i in range(len(lista)):
        print(f"PELICULA {i+1}:")
        print(f"Codigo: {lista[i]["codigo"]}")
        print(f"Nombre: {lista[i]["nombre"]}")
        print(f"Categoria: {lista[i]["categoria"]}")
        print(f"Director: {lista[i]["director"]}")
        print(f"Año: {lista[i]["año"]}")
        print("*********************************************")

def buscar_pelicula(lista):
    cod_usuario = input("Ingresa el codigo de la pelicula: ")
    encontrado = False

    for i in range(len(lista)):
        if cod_usuario==lista[i]["codigo"]:
            res = lista[i] 
            encontrado = True

    if encontrado:
        print(f"Codigo: {res["codigo"]}")
        print(f"Nombre: {res["nombre"]}")
        print(f"Categoria: {res["categoria"]}")
        print(f"Director: {res["director"]}")
        print(f"Año: {res["año"]}")
    else:
        print("No se encontro pelicula con ese codigo")


def crear_archivo(lista):
    with open("lista_peliculas.txt","w") as archivo:
        for i in lista:
            res = i["codigo"]+", "+i["nombre"]+", "+i["categoria"]+", "+i["director"]+", "+i["año"]
            archivo.write(res)

def cargar_archivo(lista):
    with open("lista_peliculas.txt","r") as archivo:
        lector = archivo.readlines()
        for i in lector:       
            res = i.split(", ")
            res[4].rstrip("\n")
            dic = {"codigo":res[0],"nombre":res[1],"categoria":res[2],"director":res[3],"año":res[4]}
            lista.append(dic)
