#!/usr/bin/env python3

from cache import *

print("--Creamos los simuladores de Caché--")

# Creo memoria de 1MB = 2^20B
memoria = list()
for i in range(2**20):
    memoria.append(0x00000)

# Cache correspondencia directa
tamanoCache = 64  # Cantidad de unidades direccionables de la cache
cantLineas  = 2   # Cantidad de lineas de la cache

cacheCorrespondencia = CacheCorrespondenciaDirecta(
    memory=memoria,
    cacheSize=tamanoCache,
    nLines=cantLineas
)

# Cache asociativa
tamanoCache = 64  # Cantidad de unidades direccionables de la cache
cantLineas  = 2   # Cantidad de lineas de la cache
politica = FIFO   # Política a usar

cacheAsociativa = CacheTotalmenteAsociativa(
    memory=memoria,
    cacheSize=tamanoCache,
    nLines=cantLineas,
    cacheAlg=politica
)

# Cache asociativa por conjuntos de n vias
tamanoCache   = 64  # Cantidad de unidades direccionables de la cache
cantVias      = 4   # Cantidad de vias
cantConjuntos = 2   # Cantidad de conjuntos
politica = FIFO     # Política a usar

cacheAsociativaNVias = CacheAsociativa_NWays(
    memory=memoria,
    cacheSize=tamanoCache,
    nWays=cantVias,
    nSets=cantConjuntos,
    cacheAlg=politica
)

print("--Uso de la Caché--")

# Muestro estado actual con el hit rate
print(cacheCorrespondencia)

# Dada una direccion, realiza un fetch
cacheCorrespondencia.fetch(0x00001)

# Contenido linea 0
cacheCorrespondencia.infoCache(line=0)

# Log de cada acceso a la memoria cache
cacheCorrespondencia.mostrarLog()

# Hit rate
cacheCorrespondencia.hitRate()

# Dada una direccion, muestra el lugar en la cache donde se encuentra
cacheCorrespondencia.getFields(0x00001)

# Cargamos un archivo con la lista de direcciones que queremos acceder
cacheCorrespondencia.fetchFrom("benchmark.list") 
