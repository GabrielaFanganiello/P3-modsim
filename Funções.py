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

#posicoes iniciais
y0b =                          
y0m =
v0m = 0
v0b = 0

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


    
Y0 = [y0b,y0m,v0m,v0b]

# Resolvendo as equações diferenciais por ODEINT
resultado = odeint(modelo,Y0,lista_t)
lista_yb = resultado[:,0]
lista_ym = resultado[:,1]
lista_vb = resultado[:,2]
lista_vm = resultado[:,3]

#Plotando os gráficos
plt.plot(lista_t,lista_yb, label)
plt.plot(lista_t,lista_ym, label)
plt.xlabel("Tempo em segundos")
plt.legend()
plt.grid(True)
plt.show()




# Validação

# Gráfico conclusivo

# Código das animações

