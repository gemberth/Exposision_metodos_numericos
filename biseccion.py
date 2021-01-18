import numpy as np
import math as m

poli=lambda x:x**10-1

#Programa principal
print ('Este programa encuentra una raíz, por el método de bisección')
xi=float(input('Introduce el valor de xi..'))
xs=float(input('Introduce el valor de xs..'))
error=float((input('Introduce el error..')))   

print('{:^10} {:^10} {:^10}  {:^10}    {:^10}  \n '.format('indice','xi','xs','Raiz','error'))
xa=(xi+xs)/2
i=0
while abs(poli(xa) ) > error:
    i=i+1
    xa = (xi+xs)/2
    if poli(xi)*poli(xa) < 0:
        xs=xa
        
    else:
        xi=xa
       
    print('{:^10} {:^10.9f} {:^10.9f} {:^10.9f}  {:^10.9f} \n '.format(i,float(xi),float(xs),float(xa),float(poli(xa))))
    #print ('La raíz es: ',xa)
