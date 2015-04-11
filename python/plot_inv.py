#!/usr/bin/python
# coding: latin-1
# La segunda línea (# coding: latin-1) es necesaria para poder usar acentos y ñ. Para entender el porqué, visitar:
# http://www.python.org/dev/peps/pep-0263/
from numpy import * 
#import pylab
import sys
import matplotlib.pyplot as plt # Primero cargo el resultado de la simulación en un arreglo:
filename_str = sys.argv[1]
data = genfromtxt(filename_str, skip_header=0,unpack=True)

# http://matplotlib.sourceforge.net/api/figure_api.html#module-matplotlib.figure 
nob_str = raw_input('Ingrese cantidad de señales a graficar: ')
# Podría preguntar aca los nombres de las señales para hacer las etiquetas
nob = int(nob_str)
totalPlots = nob
###########################
# nob subplots sharing both x/y axes
f, eje = plt.subplots(totalPlots, sharex=True, sharey=False)

#eje[0].plot(data[0], data[1])
#eje[0].set_ylabel('a0')
#eje[1].plot(data[0], data[2])
#eje[1].set_ylabel('a1')
#eje[0].set_title("Ripple Carry Adder " + str(nob) + " bits - "+ filename_str)

# Comienzo las etiquetas del resultado a partir del 3 elemento:
for i in range(0,totalPlots):
   eje[i].plot(data[0], data[i + 1])
   eje[i].set_ylabel("s"+str(i))


# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

# Escondo los ticks de todos los ejes x (menos el último):
plt.setp([a.get_xticklines() for a in f.axes[:-1]], visible=False)
# Escondo las etiquetas de todos los ticks del eje x (menos el último)
plt.setp([a.get_yticklabels() for a in f.axes[:]], visible=False)

# Con este comando aparece la ventana con los gráficos
plt.show()
