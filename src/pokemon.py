import collections
from typing import NamedTuple
import csv
from collections import namedtuple
from datetime import datetime

Pokemon=collections.namedtuple("Pokemon", "numero nombre tipo1 tipo2 HP Attk Def AttkSP DefSP Spd Gener Legend Date")


def lee_csv(fichero):
    data=[]
    with open(fichero, encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=",")
        next(reader)
        data = [Pokemon(int(numero), nombre, tipo1, tipo2, int(HP), int(Attk), int(Def), int(AttkSP), int(DefSP), int(Spd), int(Gener), bool(Legend), Date) for numero, nombre, tipo1, tipo2, HP, Attk, Def, AttkSP, DefSP, Spd, Gener, Legend, Date in reader]
        return data
        


def filtrar_por_tipo1(tipo1):
    lista=lee_csv(r'.\data\pokemon.csv')
    data=[a for a in lista if a.tipo1 == tipo1]
    return data

def filtrar_por_attk(attk):
    lista=lee_csv(r'.\data\pokemon.csv')
    data = [a for a in lista if a.Attk >= attk]
    return data

def filtrar_por_legendario(tipo1, tipo2, legendario):
    lista=lee_csv(r'.\data\pokemon.csv')
    data=[a.tipo1 for a in lista if a.tipo1 == tipo1 and a.tipo2 == tipo2 and a.Legend == legendario]
    data.append([a.tipo2 for a in lista if a.tipo2 == tipo2 and a.tipo1 == tipo1 and a.Legend == legendario])
    return data

def suma_especial(tipo1='Water', generacion=3):
    lista=lee_csv(r'.\data\pokemon.csv')
    spattk= [a.AttkSP for a in lista if a.tipo1 == tipo1 and generacion >= a.Gener]
    spdef= [a.DefSP for a in lista if a.tipo1 == tipo1 and generacion >= a.Gener]
    suma_attk=0
    suma_def=0
    for attk in spattk:
        suma_attk += attk
    for defe in spdef:
        suma_def += defe
    data = suma_attk + suma_def
    return data

def promedio_HP(legendario=True, velocidad=25):
    lista= lee_csv(r'.\data\pokemon.csv')
    dataa=[a.HP for a in lista if a.Legend == legendario and a.Spd >= velocidad]
    suma_HP=0
    for HeP in dataa:
        suma_HP += HeP
    data = suma_HP/len(dataa)
    return data
