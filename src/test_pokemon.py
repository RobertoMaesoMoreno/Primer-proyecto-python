import csv
from pokemon import lee_csv

def test_lee_csv(fichero):
    lista_pokemon= lee_csv(fichero)
    print('Total de ficheros leidos: ', len(lista_pokemon))
    print('Tres primeros: ', lista_pokemon[:3])
    print('Tres últimos: ', lista_pokemon[-3:])


print(test_lee_csv(r'.\data\pokemon.csv'))