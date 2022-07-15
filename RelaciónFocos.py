# MODULOS
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
%matplotlib inline

#----------- DATOS ---------------------------------
# lentes que se encuentran en el lab
F = np.array([11,25,25.4,35,50,75,100,125,150,200,250,300,400,500,750,1000])*10**-3
# Longitud de onda a utilizar
lamb = 776e-9
# Distintos waist
omega4= 3.3e-6
omega0=3.3e-6
omega2=19.5e-6
# focos lentes
f1=25.4e-3
f2=15e-3

def Sist_3F(F,factor, tol):
    f =[]
    idx = []
    for i in range(len(F)):
        for j in range(len(F)):
            for k in range(len(F)):
                Min = abs(F[i]*F[j]/F[k] -factor)
                if Min < tol:
                    f.append(F[i]*F[j]/F[k])
                    idx.append([F[i], F[j], F[k]])
    return f,idx, factor,Min

def Sist_2F(F,factor, tol):
    f =[]
    idx = []
    for j in range(len(F)):
        for k in range(len(F)):
            Min = abs(F[j]/F[k] - factor)
            if Min < tol:
                f.append(F[j]/F[k])
                idx.append([F[j], F[k]])
    return f,idx, Min

# Esto fue probado para construcción de dos caminos
Sist_3F(F,omega4*omega0*np.pi/lamb,  0.0001)
Sist_2F(F,omega2/omega0, 0.01)

#test
f4= omega0*omega4*f2*np.pi/(lamb*f1)
print(f4)
