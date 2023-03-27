"""
Created on Sun Mar 19 19:18:19 2023

@author: Martín Paredes
"""

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import numpy as np
import matplotlib.pyplot as plt

def mod_rlc(delta_t, x_ant, accion):
    R = 1
    L = 1
    C = 1
    A = np.array([ [-R/L, -1/L] , [1/C, 0] ])
    B = np.array([ [1/L], [0] ])
    x = np.array(x_ant)
    for i in range(1):
        xp  = A@x + B*u
        x   = x + xp*delta_t
    return x

# Ejercicio 1a

t       = np.linspace(0, 20, num=300)
tf      = 3
ten     = 12 - 8 * np.sqrt(3) * np.exp(-t/2) * np.sin( np.sqrt(3) * t/2 + np.pi/3 )
corr    = 8 * np.sqrt(3) * np.exp(-t/2) * np.sin( np.sqrt(3)*t/2 )

# Ejercicio 1b

X       = np.array([ [0], [0] ])
paso    = 0.1
u       = 12 
x1      = [] # Corriente
x2      = [] # Voltaje
acc     = [] # Acción
n       = tf/paso

for i in range(int(n)):
  x1.append(X[0]) # Corriente
  x2.append(X[1]) # Voltaje
  X = mod_rlc(paso, X, u) 
  acc.append(u)

t2 = np.linspace(0, tf, num=int(n))

# Gráficas

fig, ax = plt.subplots(dpi=400)
ax.plot(t,ten, label='Analítica')
ax.plot(t2,x2,'.', color='red', label='Euler')
ax.legend(loc='upper right',ncol=1)
ax.set_xlim(0.0,tf)
ax.set_ylim(0.0,18.0)
ax.set_title('Tensión (voltaje) del capacitor')
ax.set_xlabel('t [s]')
ax.set_ylabel('Vc [V]')
plt.grid(visible = True, which = 'both', axis = 'both')
plt.savefig('Ejercicio-1a-1b_tension.png', dpi=400, format='png', orientation='landscape')

fig, bx = plt.subplots(dpi=400)
bx.plot(t,corr, label='Analítica')
bx.plot(t2,x1,'.',color='red', label='Euler')
bx.legend(loc='upper right',ncol=1)
bx.set_xlim(0.0,tf)
bx.set_ylim(-2.0,8.0)
bx.set_title('Corriente')
bx.set_xlabel('t [s]')
bx.set_ylabel('I [A]')
plt.grid(visible = True, which = 'both', axis = 'both')
plt.savefig('Ejercicio-1a-1b_corriente.png', dpi=400, format='png', orientation='landscape')
plt.show()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ejercicio 2

import numpy as np
import matplotlib.pyplot as plt

'''
Las soluciones analíticas son

- Tensión:
    v(t) = 12 - 0.00024794925315873*exp(-219995454.451536*t)
    -12.0002479492532*exp(-4545.5484636724⋅t)

- Corriente:
    i(t) = 8.67361737988404*exp(-19) 
    - 0.00545477086295743*exp(-219995454.451536*t)
    + 0.00545477086295742*exp(-4545.5484636724*t)
'''
    
t       = np.linspace(0, 0.005,num=501)
ten     = 12 - 0.000247949253158732*np.exp(-219995454.451536*t)\
    -12.0002479492532*np.exp(-4545.5484636724*t)
corr    = 8.67361737988404e-19\
    - 0.00545477086295743*np.exp(-219995454.451536*t)\
    + 0.00545477086295742*np.exp(-4545.5484636724*t)

fig, ax = plt.subplots(dpi=400)
ax.plot(t,ten)
ax.set_title('Tensión (voltaje) del capacitor')
ax.set_xlabel('t [s]')
ax.set_ylabel('Vc [V]')
plt.grid(visible = True, which = 'both', axis = 'both')
plt.savefig('Ejercicio-2_tension.png', dpi=400, format='png', orientation='landscape')

fig, bx = plt.subplots(dpi=400)
bx.plot(t,corr)
bx.set_title('Corriente')
bx.set_xlabel('t [s]')
bx.set_ylabel('I [A]')
plt.grid(visible = True, which = 'both', axis = 'both')
plt.savefig('Ejercicio-2_corriente.png', dpi=400, format='png', orientation='landscape')
plt.show()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ejercicio 3

import numpy as np
import matplotlib.pyplot as plt

'''
Las soluciones analíticas son

- Tensión:
    v(t) = 12 - 0.00024794925315873*exp(-219995454.451536*t)
    -12.0002479492532*exp(-4545.5484636724⋅t)

- Corriente:
    i(t) = 8.67361737988404*exp(-19) 
    - 0.00545477086295743*exp(-219995454.451536*t)
    + 0.00545477086295742*exp(-4545.5484636724*t)
'''

n       = 100
t       = np.linspace(0, 0.001,num=n+1)
tiempo  = np.linspace(0, 0.006,num=6*n+1)
k1      = 1
k2      = 0
ten     = [0]
corr    = [0]
for i in range(6):
    for j in range(n):
        if i%2 == 0:
            ten.append(12 - 0.000247949253158732*np.exp(-219995454.451536*t[j])\
                       - 12.0002479492532*np.exp(-4545.5484636724*t[j]))
            corr.append(8.67361737988404e-19\
                        - 0.00545477086295743*np.exp(-219995454.451536*t[j])\
                        + 0.00545477086295742*np.exp(-4545.5484636724*t[j]))
        else:
            ten.append(- 12 - 0.000247949253158732*np.exp(-219995454.451536*t[j])\
                       + 12.0002479492532*np.exp(-4545.5484636724*t[j]))
            corr.append(- 8.67361737988404e-19\
                        + 0.00545477086295743*np.exp(-219995454.451536*t[j])\
                        - 0.00545477086295742*np.exp(-4545.5484636724*t[j]))

fig, ax = plt.subplots(dpi=400)
ax.plot(tiempo,ten)
ax.set_ylim(-14.0,14.0)
ax.set_title('Tensión (voltaje) del capacitor')
ax.set_xlabel('t [s]')
ax.set_ylabel('Vc [V]')
plt.grid(visible = True, which = 'both', axis = 'both')
plt.savefig('Ejercicio-3_tension.png', dpi=400, format='png', orientation='landscape')

fig, bx = plt.subplots(dpi=400)
bx.plot(tiempo,corr)
bx.set_ylim(-0.006,0.006)
bx.set_title('Corriente')
bx.set_xlabel('t [s]')
bx.set_ylabel('I [A]')
plt.grid(visible = True, which = 'both', axis = 'both')
plt.savefig('Ejercicio-3_corriente.png', dpi=400, format='png', orientation='landscape')
plt.show()