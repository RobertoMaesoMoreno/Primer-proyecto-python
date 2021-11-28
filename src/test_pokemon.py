import csv
from pokemon import lee_csv
from pokemon import filtrar_por_tipo1
from pokemon import filtrar_por_attk
from pokemon import filtrar_por_legendario
from pokemon import suma_especial
from pokemon import promedio_HP

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

#print(test_lee_csv(r'.\data\pokemon.csv'))
#print(filtrar_por_tipo1('Poison'))
#print(filtrar_por_attk(50))
#print(filtrar_por_legendario('Dragon', 'Psychic', True))
#print(suma_especial())
#print(promedio_HP())


#print(test_filtrar_por_tipo1('Poison'))
#print(test_filtrar_por_attk(50))
#print(test_filtrar_por_legendario('Dragon', 'Psychic', True))
#print(test_suma_especial())
print(promedio_HP())



