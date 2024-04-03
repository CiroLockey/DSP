import numpy as np


#Ejercicio 4 a

mediciones = np.random.random(size = (5,20))    

for i in range(5):
    print(f'Medicion nº: {i}')
    print(mediciones[:,i])


## La corrección fue agregar range al ciclo for. El original era for i in 5. 

#Ejercicio 4 b
#Se pide guardar los máximos y mínimos de cada medición.

mediciones_max=[]
mediciones_min=[]

for i in range(5):

    mediciones_max.append(max(mediciones[:,i]))
    mediciones_min.append(min(mediciones[:,i]))


print("max ", mediciones_max)
print("min ", mediciones_min)



#Ejercicio 5

