from cache import CacheCorrespondenciaDirecta
import numpy as np
import pylab

# Correspondencia directa, vario distintas lineas
# y guardo el hit rate para cada configuracion
# usando la secuencia de fetchs definida en benchmark.list
lines = [1, 2, 4]  # Poner el numero de lineas a testear
res = []
for l in lines:
    ca = CacheCorrespondenciaDirecta(
                               memory=list(range(0, 2**16)),
                               cacheSize=128, nLines=l)
    ca.fetchFrom('benchmark.list')
    res.append(ca.hitRate())
    print(("Lineas:", l, "HitRate:", ca.hitRate()))

# res tiene los distintos valores de
# hit rates para cada configuracion

# uso pylab para plotear
pylab.plot(lines, res, '.-', lw=2,
           label='CacheCorrespondenciaDirecta - FIFO')
pylab.title('Cache Correspondencia Directa', size=16)
pylab.xlabel('Lineas', size=16)
pylab.ylabel('Hit Rate', size=16)

pylab.xlim([0, np.max(lines)])
pylab.xticks(size=16)
pylab.yticks(size=16)
pylab.show()
