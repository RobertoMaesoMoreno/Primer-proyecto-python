import collections
from typing import NamedTuple
import csv
from collections import namedtuple

pokemon=collections.namedtuple("Pokemon", "numero nombre tipo1 tipo2 HP Attk Def AttkSP DefSP Spd Gener Legend Date")


def lee_csv(fichero):
    data=[]
    with open(fichero, encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=",")
        next(reader)
        for numero, nombre, tipo1, tipo2, HP, Attk, Def, AttkSP, DefSP, Spd, Gener, Legend, Date in reader:
            numero = int(numero)
            nombre = str(nombre)
            tipo1 = str(tipo1)
            tipo2 = str(tipo2)
            HP = int(HP)
            Attk = int(Attk)
            Def = int(Def)
            AttkSP =int(AttkSP)
            DefSP =int(DefSP)
            Spd = int(Spd)
            Gener = str(Gener)
            Legend = bool(Legend)
            Date = str(Date)
            Tupla= pokemon(numero, nombre, tipo1, tipo2, HP, Attk, Def, AttkSP, DefSP, Spd, Gener, Legend, Date)
            data.append(Tupla)
        return data
        
            

