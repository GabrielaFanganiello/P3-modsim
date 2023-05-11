# Tema
    # Pendulo elastico 2d

# Importando bibliotecas necessárias

from scipy.integrate import odeint
from math import *
import numpy as np
import matplotlib.pyplot as plt

# Dados experimentais


# Simplificações feitas / abstração

    # Objeto considerado um ponto material
    # Considera resistência do ar

    # Objetivo: quanto tempo demora para um pendulo de diferentes massas parar?


# Condições iniciais, variáveis globais e fórmulas

g = 9.8                             # Aceleração da gravidade [m/s2]

m = 0                                # Massa da esfera [kg]

r =   0                              # Raio da esfera [m]

k =   0                              # Constante elástica da mola [N/m]

rho =   0                            # Densidade do ar [kg/m3]

A = 4 * pi*(r**2)                       # Área da esfera [m2]

Cd =   0                             # Coeficiente de arrasto []

l0 =   0                             # Comprimento inicial da mola []

#posicoes iniciais
x0 =   0                       
y0 = 0
vx0 = 0
vy0 = 0

CI = [x0, y0, vx0, vy0]


tempo = np.arange(0, )                 # Lista de tempo


# Implementando função do modelo

def modelo(c0, tempo):

    x = c0[0]
    y = c0[1]
    vx = c0[2]
    vy = c0[3]

    l = ((x**2)+(y**2))**0.5                        # Comprimento da mola
    Fel = k * (l - l0)
    seno_theta = x/l            # seno theta (ângulo entre força elástica e eixo x)
    cosseno_theta = y/l          # cosseno theta (ângulo entre força elástica e eixo y)

    Dx = (1/2) * rho * A * Cd * vx * ((vx**2)+(vy**2)**0.5)    # Fórmula do arrasto decomposta no eixo x
    Dy = (1/2) * rho * A * Cd * vy * ((vx**2)+(vy**2)**0.5)    # Fórmula do arrasto decomposta no eixo y

    dxdt = vx
    dydt = vy

    dvxdt = 1/m(-Fel*seno_theta - Dx)
    dvydt = 1/m(Fel*cosseno_theta - Dy - m*g)

    dXdt = [dxdt, dydt, dvxdt, dvydt]
    
    return dXdt
    
resultado = odeint(modelo, CI, tempo)
lista_x = resultado[:,0]
lista_y = resultado[:,1]
lista_vx = resultado[:,2]
lista_vy = resultado[:,3]

plt.plot(lista_x,lista_y)
plt.xlabel("Deslocamento da mola")
plt.grid(True)
plt.show()


# Plotando os gráficos

# Validação

# Gráfico conclusivo

# Código das animações