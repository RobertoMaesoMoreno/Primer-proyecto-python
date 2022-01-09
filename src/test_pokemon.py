import csv
from pokemon import diccionario_generacion, lee_csv
from pokemon import filtrar_por_tipo1
from pokemon import filtrar_por_attk
from pokemon import filtrar_por_legendario
from pokemon import suma_especial
from pokemon import promedio_HP
from pokemon import mayor_velocidad
from pokemon import mayor_ataque
from pokemon import diccionario_generacion
from pokemon import diccionario_max_legendario


def test_lee_csv(fichero):
    lista_pokemon= lee_csv(fichero)
    print('Total de ficheros leidos: ', len(lista_pokemon))
    print('Tres primeros: ', lista_pokemon[:3])
    print('Tres últimos: ', lista_pokemon[-3:])

def test_filtrar_por_tipo1(tipo1):
    lista_pokemon = filtrar_por_tipo1(tipo1)
    print('Total de ficheros leidos: ', len(lista_pokemon))
    print('Tres primeros: ', lista_pokemon[:3])
    print('Tres últimos: ', lista_pokemon[-3:])

def test_filtrar_por_attk(attk):
    lista_pokemon= filtrar_por_attk(attk)
    print('Total de ficheros leidos: ', len(lista_pokemon))
    print('Tres primeros: ', lista_pokemon[:3])
    print('Tres últimos: ', lista_pokemon[-3:])

def test_filtrar_por_legendario(tipo1,tipo2,legendario):
    lista_pokemon= filtrar_por_legendario(tipo1,tipo2,legendario)
    print('Total de ficheros leidos: ', len(lista_pokemon))
    print('Tres primeros: ', lista_pokemon[:3])
    print('Tres últimos: ', lista_pokemon[-3:])

def test_suma_especial(tipo1='Water',generacion=3):
    lista_pokemon= suma_especial(tipo1,generacion)
    print(lista_pokemon)

def test_mayor_ataque(velocidad):
    lista_pokemon= suma_especial(tipo1,generacion)
    print(mayor_ataque(velocidad))

def test_mayor_velocidad(n):
    print(mayor_velocidad(n))
    print('Tres últimos: ', lista_pokemon[-3:])
