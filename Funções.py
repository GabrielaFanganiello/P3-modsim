# Tema
    # Pendulo elastico 2d

# Importando bibliotecas necessárias

from math import pi
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

    dxdt = vx
    dydt = vy

    dvxdt = 1/m()
    dvydt = 

    dXdt = [dxdt, dydt, dvxdt, dvydt]

    return dXdt

# Resolvendo as equações diferenciais por ODEINT

#Plotando os gráficos

# Validação

# Gráfico conclusivo

# Código das animações

