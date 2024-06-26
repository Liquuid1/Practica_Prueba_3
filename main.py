import fun
from os import system, stat

op = 0 #opcion que ingresa el usuario para interactuar con el menu
peliculas = [] #lista de peliculas vacia, aqui se guardaran los diccionarios

#Esto verifica si el archivo esta NO esta vacio, si no esta vacio, se sube lo que esta en el archivo a lista peliculas
if stat('lista_peliculas.txt').st_size != 0: 
    fun.cargar_archivo(peliculas)


while op !=4:
    system("cls")
    fun.mostrar_menu()
    op = fun.get_opcion()

    if op == 1:
        system("cls")
        peliculas.append(fun.agregar_pelicula())
    elif op == 2:
        system("cls")
        fun.listar_peliculas(peliculas)
        system("pause")
    elif op == 3:
        system("cls")
        fun.buscar_pelicula(peliculas)
        system("pause")

fun.crear_archivo(peliculas)
