# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  21/22)
Autor/a: Roberto Maeso Moreno;   uvus:&lt;robmamemor&gt;


El proyecto tiene como objetivo analizar los datos de pokemons publicados en el dataset que se ha proporcionado a los alumnos. El dataset original tiene 13 columnas.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **pokemon.py**: Contiene funciones para explotar los datos sobre los pokemon.
    * **test_pokemon.py**: Contiene funciones de test para probar las funciones del módulo `pokemon.py`. En este módulo está el main. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **pokemon.csv**: Archivo con los datos de pokemon que van a ser explotados.
        
## Estructura del *dataset*

Cada fila del dataset recoge los datos de los pokemon, siendo:

nombre, tipo1, tipo2, HP, Attk, Def, AttkSP, DefSP, Spd, Gener, Legend, Date

* **numero**: de tipo int, es un identificador entero.
* **nombre**: de tipo str, representa el nombre del pokemon.
* **HP**: de tipo int, representa sus puntos de vida.
* **Attk**: de tipo int, representa sus puntos de ataque.
* **Def**: de tipo int, representa sus puntos de defensa.
* **AttkSP**: de tipo int, representa sus puntos de ataque especial.
* **Spd**: de tipo int, representa sus puntos de velocidad.
* **Gener**: de tipo int, representa a qué generación pertenece.
* **Legend**: de tipo booligan, representa si es legendario o no.
* **Date**: de tipo str, representa la fecha.

## Tipos implementados

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

`pokemon=collections.namedtuple("Pokemon", "numero nombre tipo1 tipo2 HP Attk Def AttkSP DefSP Spd Gener Legend Date")`

en la que los tipos de cada uno de los campos son los siguientes:

`Info(int, str, str, str, int, int, int, int, int, int, int, bool, str)`

## Funciones implementadas
En este proyecto se han implementado las siguientes funciones, que están clasificadas según los bloques y tipos de funciones que se requieren en cada una de las entregas.
El módulo principal es el módulo pokemon.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.
### Módulo pokemon

#### Entrega 1

* **Bloque 0**  
  * **lee_csv(fichero)**: lee los datos del fichero csv y devuelve una lista de tuplas de tipo Pokemon con los datos del fichero.

#### Entrega 2
* **Bloque 2**
  * **filtrar_por_tipo1(tipo1)**: filtra los datos del fichero csv por el primer tipo elemental de Pokemon que se le proporciona a la función.
  
  * **filtrar_por_attk(attk)**: filtra los datos del fichero csv, devolviendo en una lista los que su ataque sea mayor que el propocionado a la función.

  * **filtrar_por_legendario(tipo1, tipo2, legendario)**: devuelve una lista con los tipos de los Pokémon que se le proporcione a la función según si se le indique si son legendarios o no en la misma.

* **Bloque 3**

  * **suma_especial(tipo1, generacion)**: suma todos los parámetros de ataque especial y defensa especial del tipo que se le proporcione a la función a partir de la generación que se indique.

  * **promedio_HP(legendario, velocidad)**: da una media del HP de todos los Pokemon indicando en la función si se filtra por legendarios o los que no lo son y si su velocidad supera la proporcionada en la función.

### Módulo test_pokemon
En el módulo de pruebas se han definido las siguientes funciones de pruebas, cada una de las cuales se usa para probar la función con que tiene el mismo nombre. Por ejemplo, la función `test_lee_csv` prueba la función `lee_csv`.

* **test_lee_csv(fichero)**
* **test_filtrar_por_tipo1(tipo1)**
* **test_filtrar_por_attk(attk)**
* **test_filtrar_por_legendario(tipo1,tipo2,legendario)**
* **test_suma_especial(tipo1='Water',generacion=3)**