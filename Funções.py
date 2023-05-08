# Tema
    # Pendulo elastico 2d

# Importando bibliotecas necessárias

from math import pi
import numpy as np

# Dados experimentais


# Simplificações feitas / abstração

    # Objeto considerado um ponto material
    # Considera resistência do ar
    # Eixo xy: origem na extremidade fixa da mola, com eixo x para direita e eixo y para cima

    # Objetivo: quanto tempo demora para um pendulo de diferentes massas parar?


# Condições iniciais, variáveis globais e fórmulas

g = 9.8                             # Aceleração da gravidade [m/s2]

m =                                 # Massa da esfera [kg]

r =                                 # Raio da esfera [m]

k =                                 # Constante elástica da mola [N/m]

rho =                               # Densidade do ar [kg/m3]

A = pi*(r**2)                       # Área [m2]

Cd =                                # Coeficiente de arrasto []

tempo = np.arange()                 # Lista de tempo


# Implementando função do modelo

def modelo(c0, tempo):

    x = c0[0]
    y = c0[1]
    vx = c0[2]
    vy = c0[3]

    l = ((x**2)+(y**2))**0.5                        # Comprimento da mola
    seno_Fel = x/(((x**2)+(v**2))**0.5)             # seno theta (ângulo entre força elástica e eixo x)
    cosseno_Fel = y/(((x**2)+(y**2))**0.5)          # cosseno theta (ângulo entre força elástica e eixo y)

    Dx = 1/m(rho*A*Cd*vx*((vx**2)+(vy**2)**0.5))    # Fórmula do arrasto decomposta no eixo x
    Dy = 1/m(rho*A*Cd*vy*((vx**2)+(vy**2)**0.5))    # Fórmula do arrasto decomposta no eixo y

    dxdt = vx
    dydt = vy

    dvxdt = 1/m(-(Fel*seno_Fel)-Dx)
    dvydt = 1/m(-(Fel*cosseno_Fel)-Dy-(m*g))

    dXdt = [dxdt, dydt, dvxdt, dvydt]

    return dXdt

# Resolvendo as equações diferenciais por ODEINT
resultado = odeint(modelo,c0,tempo)
lista_x = resultado[:,0]
lista_y = resultado[:,1]
lista_vx = resultado[:,2]
lista_vy = resultado[:,3]

#Plotando os gráficos
plt.plot(tempo,lista_y, label='')
plt.plot(tempo,lista_y, label='')
plt.xlabel("Tempo em segundos")
plt.legend()
plt.grid(True)
plt.show()



# Plotando os gráficos

# Validação

# Gráfico conclusivo

# Código das animações

