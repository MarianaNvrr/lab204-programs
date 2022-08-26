# MODULOS
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
%matplotlib inline

#----------- DATOS ---------------------------------
# focos de las lentes que se encuentran en el lab
F = np.array([7.5,8,10,11,25,25.4,35,50,75,100,125,150,200,250,300,400,500,750,1000])*10**-3
# Longitud de onda a utilizar
lamb = 775e-9

#Focusing parameter
chi=0.1

#Largo del cristal
L = 3.1e-3

# Distintos waist
omega4= 3.3e-6
omega0_singlecore=6.6e-6 #fibra 780
omega0_multicore = 9.2e-6 #fibra 4-nucleos 1500
omega2_cristal = np.sqrt(lamb*L/(2*np.pi*chi))

# focos lentes
f1=25.4e-3
f2=15e-3

#----------- funciones ---------------------
def Sist_3F(F,factor, tol):
    '''
    Función que me relaciona los focos de tres lentes de la forma
    R = f2*f3/f1

    Inputs:
        F (lista): focos de las lentes en el lamb
        factor (float): número al que queremos que R sea igual
        tol (float): tolerancia
    return:
        f (float): f2*f3/f1 que es la magnificación
        factor (float): me da el valor de f3, f2 y f1
    '''
    f =[]
    idx = []
    for i in range(len(F)):
        for j in range(len(F)):
            for k in range(len(F)):
                Min = abs(F[i]*F[j]/F[k] -factor)
                if Min < tol:
                    f.append(F[i]*F[j]/F[k])
                    idx.append([F[i], F[j], F[k]])
    return f,idx

def Sist_2F(F,factor, tol):
    '''
    Función que me relaciona los focos de dos lentes de la forma
    R = f2/f1

    Inputs:
        F (list): focos de las lentes en el lamb
        factor (float): número al que queremos que R sea igual
        tol (float): tolerancia
    return:
        f (float): f2/f1 que es la magnificación
        factor (float): me da el valor de f2 y f1
    '''
    f =[]
    idx = []
    for j in range(len(F)):
        for k in range(len(F)):
            Min = abs(F[j]/F[k] - factor)
            if Min < tol:
                f.append(F[j]/F[k])
                idx.append([F[j], F[k]])
    return f,idx
#---------------

#Evaluamos las funciones
Sist_3F(F,omega4*omega0*np.pi/lamb,  0.0001)
Sist_2F(F, omega2/omega0_singlecore, 0.01)
