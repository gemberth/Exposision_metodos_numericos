import numpy as np
import math as ma

#ingreso  x**2-m.cos(x) x**3 +4*(x**2)-10
fx = lambda x: x**2-ma.cos(x)

x_i=-1
x_f=-0.5
tolera=0.001
i=0
#Procedimiento
error=abs(x_f-x_i)
ea=0
ea1=0
print('{:^10} {:^10} {:^10}  {:^10}    {:^10}  '.format('i','xi','xf','Raiz','Error'))


#La variable error es la del error absoluto 

while not(error<=tolera):
    
    fa=fx(x_i)
    fb=fx(x_f)
    c= x_f - fb*(x_i-x_f)/(fa-fb)
    fc=fx(c)
    cambio=np.sign(fa)*np.sign(fc)
    
    if cambio>0:
        error=abs(c-x_i)
        #ea=tramo
        #ea1=(ea ,x_i)
        #tramo=tramo/x_i
        #tramo=tramo*100
        #tramo=tramo*100#(c-x_i)
        #tramo=((x_i-x_f)/x_i)
        x_i=c
    
    else:
        error = abs(((x_f-c)/(x_f))*100)
        x_f=c
        
    i=i+1
    print('{:^10} {:.10f} {:^10.1f} {:^10.9f}   {:.10f} '.format(i,float(x_i),float(x_f),float(c),float(error)))
    #print('La raiz se encuentra en {:.10f}'.format(c))
    #print('Error estimado de  {:.10f}'.format(tramo))
    #print('El numero de iteraciones son ',i)
