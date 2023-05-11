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

def modelo(lista,tempo):
    x = lista[0]
    y = lista[1]
    vx = lista[2]
    vy = lista[3]
    
    l = (x**2 + y**2)**0.5
    Fel = k*(l-l0)
    seno = x/l
    cos = y/l
    
    dxdt = vx
    dydt = vy
    dvxdt = 1/m*(-(Fel*seno)-0.5*p*A*Cd*vx*(vx**2+vy**2)**0.5)
    dvydt = 1/m*(-(Fel*seno)-0.5*p*A*Cd*vx*(vx**2+vy**2)**0.5)-m*g
    
    dXdt = [dxdt, dydt, dvxdt, dvydt]
    
    return dXdt
    
Y0 = [y0b,y0m,v0m,v0b]
resultado = odeint(modelo,Y0,lista_t)
lista_yb = resultado[:,0]
lista_ym = resultado[:,1]
lista_vb = resultado[:,2]
lista_vm = resultado[:,3]

plt.plot(lista_t,lista_yb)
plt.plot(lista_t,lista_ym)
plt.xlabel("Tempo em segundos")
plt.legend()
plt.grid(True)
plt.show()

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

