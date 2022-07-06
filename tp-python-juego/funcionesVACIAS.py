from principal import *
from configuracion import *
import random
import math
import re

def tiempo(cadena):
    for elem in cadena:
        if elem==":":
            return True
    return False
def numeros(elemento):
    for x in range(1,1030):
        if elemento==(str(x))+"\n":
            return True
    return False
def espacio(elemento):
    if elemento=="\n":
        return True
    return False


def limpiar_etiquetas(pal): #elimina las italicas
    cleanr=re.compile('<.*?>')
    pallimpia=re.sub(cleanr," ",pal)
    clean2=re.compile('\n')
    pallimpia2=re.sub(clean2,'',pallimpia)
    return pallimpia2

def lectura(archivo, subtitulo,n): #se queda solo con los subtitulo de cierta longitud y filtra
    lista=archivo.readlines()
    lista2=[]
    for x in range(len(lista)-3):
        if  not tiempo(lista[x]) and not espacio(lista[x]) and not numeros(lista[x]) :
            subtitulo.append(limpiar_etiquetas(lista[x]))
    return subtitulo

def seleccion(subtitulo):
    #elige uno al azar, lo devuelve, el siguiente y otro
    indice=random.randint(0,len(subtitulo)) #toma valor al azar
    azar=subtitulo[indice]
    siguiente=subtitulo[indice+1]
    indice=random.randint(0,len(subtitulo))
    otro=subtitulo[indice]
    lista=[azar,siguiente,otro]
    return lista

def puntos(n):
    n=n*2
    return n

def procesar(palabraUsuario,mostrada,siguiente, otra,correctas):
    punt=0
    if palabraUsuario.lower() in siguiente.lower():#si palabraUsuario esta dentro de (o es igual a) siguiente
        punt=punt+1 # 1 a la racha de acertadas
        if correctas>1:
         return puntos(punt)
        return punt
    return -1


