# Tema
    # Pendulo elastico 2d

# Importando bibliotecas necessárias

from math import *

import numpy as np

# Dados experimentais


# Simplificações feitas / abstração

# Condições iniciais, variáveis globais e fórmulas

g = 9.8                             # Aceleração da gravidade [m/s2]

m =                                 # Massa da esfera [kg]

r =                                 # Raio da esfera [m]

k =                                 # Constante elástica da mola [N/m]

rho =                               # Densidade do ar [kg/m3]

A = pi*(r**2)                       # Área [m2]

Cd =                                # Coeficiente de arrasto []

D = 1/2(rho * Cd * A * v**2)        # Fórmula do arrasto

tempo = np.arange()                 # Lista de tempo


# Implementando função do modelo

def modelo(c0, tempo):

    x = c0[0]
    y = c0[1]
    vx = c0[2]
    vy = c0[3]

    l = (x**2 + y**2)**0.5
    Fel = k*(l-l0)
    seno = x/l
    cos = y/l

    dxdt = vx
    dydt = vy
    dvxdt = 1/m*(-(Fel*seno)-0.5*rho*A*Cd*vx*(vx**2+vy**2)**0.5)
    dvydt = 1/m*((Fel*cos)-0.5*rho*A*Cd*vx*(vx**2+vy**2)**0.5)-m.g
    

    dc0dt = [dxdt, dydt, dvxdt, dvydt]

    return dc0dt

# Resolvendo as equações diferenciais por ODEINT

#Plotando os gráficos

# Validação

# Gráfico conclusivo

# Código das animações

