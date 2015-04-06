#!/usr/bin/python
# coding: latin-1
# La segunda línea (# coding: latin-1) es necesaria para poder usar acentos y ñ.
from numpy import * 
import sys
import matplotlib.pyplot as plt # Primero cargo el resultado de la simulación en un arreglo:
filename_str = sys.argv[1]
data = genfromtxt(filename_str, skip_header=0,unpack=True)

# Cualquier duda, leer la documentación sobre matplotlib
# http://matplotlib.sourceforge.net/api/figure_api.html#module-matplotlib.figure 
# Para ver ejemplos de qué se puede graficar: http://matplotlib.org/gallery.html

#######################################
#
# Sección de configuración:
#
#######################################
Vds = data[0]
Vgs = data[2]
Id = iter(data[3])	# Aca estan todas las corrientes de todos los Vg 
			# uso 'iter' para poder ir sacando de a uno los valores con Id.next() 



###########################
# Creo una lista con las señales de Id, una lista por cada Vg
###########################

valores = [[]]	# Inicializo una lista de listas, vacia
curva=0		# Indice que hace referencia un valor de Vg
oldVal = Vgs[0]	# Valor que comparo para saber si estoy en la misma curva del Vg
Vg = [oldVal]	# Lista donde guardo los distintos valores de Vg utilizados

for x in Vgs:
	if(x != oldVal):
		curva=curva+1	# Si el Vg es distinto, nuevo índice de curva
		valores.append([])	# y creo una lista vacía para el nuevo Id
		Vg.append(x)	# Agrego nuevo valor de Vg
	oldVal = x
	valores[curva].append(Id.next())

####
# Graficamos todas las curvas, una por cada Vg
####
Vd = Vds[:len(valores[0])]	#Esto es para el eje de las x
for i in range(0,len(valores)):
		plt.plot(Vd,valores[i],label="Vgs={}".format(Vg[i]))


##########
# Opciones para ubicar el cuadro con las leyendas
##########
plt.legend(loc="upper right", bbox_to_anchor=[1, 1],
		           ncol=2, shadow=True, title="Vgs", fancybox=True)

##########
# Opciones para etiquetas de los ejes y el título
##########
plt.title("Ids-Vds")
plt.ylabel("Ids")
plt.xlabel("Vds")


#########
# Opciones para la grilla
#########
plt.grid(True)	# Hay muchas opciones, dejamos todo por defecto.


########
# Ejemplo de cómo agregar texto en el gráfico
########
plt.text(1.20,-2.35E-4,"Vgs = 1.98 V")

######################################################################
# Con este comando aparece la ventana con los gráficos.
######################################################################
plt.show()	

