import os

#Muestra el menu para que el usuario interactue
def mostrar_menu():
    menu = """[1] Agregar pelicula
[2] Listar peliculas
[3] Buscar pelicula
[4] Salir
--> """
    print(menu,end="")
    
#Permite que el usuario ingrese su opción, controla errores de entrada
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

#Le pide al usuario los datos de la pelicula y devuelve un diccionario con la pelicula
def agregar_pelicula():
    #Le pide al usuario los datos
    cod = input("Ingresa el codigo de la pelicula: ")
    nombre = input("Ingresa el nombre de la pelicula: ")
    categoria = input("Ingresa la categoria de la pelicula: ")
    director = input("Ingresa el director de la pelicula: ")
    anio = input("Ingresa el año de la pelicula: ")

    #Guarda los datos que ingreso el usuario como un diccionario en 'res'
    res = {"codigo":cod,"nombre":nombre,"categoria":categoria,"director":director,"año":anio}
    #Retorna 'res'
    return res

#Muestra todas las peliculas ingresadas por pantalla, la función requiere que le pasen la lista de peliculas como argumento
def listar_peliculas(lista):
    #Se recorre todo el rango de la lista para mostrar todas las peliculas
    for i in range(len(lista)):
        #Se imprime la cabecera del mensaje.
        print(f"PELICULA {i+1}:")

        #Se imprime el diccionario guardado en la lista, como segundo parametro se le pasa la KEY del valor que se quiere mostrar
        print(f"Codigo: {lista[i]["codigo"]}")
        print(f"Nombre: {lista[i]["nombre"]}")
        print(f"Categoria: {lista[i]["categoria"]}")
        print(f"Director: {lista[i]["director"]}")
        print(f"Año: {lista[i]["año"]}")
        print("*********************************************")

#Busca la pelicula en la lista mediante el codigo, requiere que se le pase la lista de peliculas como argumento
def buscar_pelicula(lista):
    #El usuario ingresa el codigo
    cod_usuario = input("Ingresa el codigo de la pelicula: ")
    #Se inicia una variable para saber si se ha encontrado la pelicula o no
    encontrado = False

    #Se recorre toda la lista buscando el codigo en los diccionarios con la KEY "codigo"
    for i in range(len(lista)):
        #Si se encuentra el codigo, se guarda ese diccionario con la pelicula y encontrado pasa a True
        if cod_usuario==lista[i]["codigo"]:
            res = lista[i] 
            encontrado = True

    #Si se encontro la pelicula se imprime, si no se le indica al usuario que no existe.
    if encontrado:
        print(f"Codigo: {res["codigo"]}")
        print(f"Nombre: {res["nombre"]}")
        print(f"Categoria: {res["categoria"]}")
        print(f"Director: {res["director"]}")
        print(f"Año: {res["año"]}")
    else:
        print("No se encontro pelicula con ese codigo")


#Crea un archivo para guardar las peliculas ingresadas
def crear_archivo(lista):
    with open("lista_peliculas.txt","w") as archivo:
        #Se recorre la lista y se guarda en el archivo
        for i in lista:
            res = i["codigo"]+", "+i["nombre"]+", "+i["categoria"]+", "+i["director"]+", "+i["año"]+"\n"
            archivo.write(res)

#Carga los datos que hay en el archivo a la lista de las peliculas
def cargar_archivo(lista):
    with open("lista_peliculas.txt","r") as archivo:
        #Se guarda cada linea del archivo como una entrada en la lista lector
        lector = archivo.readlines()
        #Se recorre la lista lector
        for i in lector:       
            #Se separa la lista por el valor ", "
            res = i.split(", ")
            #En la última posición se la lista res se le borra el salto de linea.
            res[4] = res[4].rstrip("\n")
            #Se guarda todo como un diccionario
            dic = {"codigo":res[0],"nombre":res[1],"categoria":res[2],"director":res[3],"año":res[4]}
            #Se agrega el diccionario a la lista
            lista.append(dic)
