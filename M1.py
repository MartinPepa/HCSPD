"""
Created on Sun Mar 19 19:18:19 2023

@author: Martín Paredes
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy

#%%

# Ejercicio 1a
t       = np.linspace(0, 20, num=201)
ten     = 12 - 8 * np.sqrt(3) * np.exp(-t/2) * np.sin( np.sqrt(3) * t/2 + np.pi/3 )
corr    = 8 * np.sqrt(3) * np.exp(-t/2) * np.sin( np.sqrt(3)*t/2 )

fig, ax = plt.subplots(dpi=300)
ax.plot(t,ten)
ax.set_xlim(0.0,20.0)
ax.set_ylim(0.0,15.0)
ax.set_title('Tensión (voltaje) del capacitor')
ax.set_xlabel('t [s]')
ax.set_ylabel('Vc [V]')
plt.grid(visible = True, which = 'both', axis = 'both')

fig, bx = plt.subplots(dpi=300)
bx.plot(t,corr)
bx.set_xlim(0.0,20.0)
bx.set_ylim(-2.0,7.0)
bx.set_title('Corriente')
bx.set_xlabel('t [s]')
bx.set_ylabel('I [A]')
plt.grid(visible = True, which = 'both', axis = 'both')
plt.show()


# Ejercicio 1b


#%%

# Ejercicio 2
# ATENCIÓN: PENDIENTE DE CHEQUEAR
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
    
t       = np.linspace(0, 0.1,num=100)
ten     = 12 - 0.00024794925315873*np.exp(-219995454.451536*t)\
    -12.0002479492532*np.exp(-4545.5484636724*t)
corr    = 8.67361737988404e-19\
    - 0.00545477086295743*np.exp(-219995454.451536*t)\
    + 0.00545477086295742*np.exp(-4545.5484636724*t)

fig, ax = plt.subplots(dpi=300)
ax.plot(t,ten)
#ax.set_xlim(0.0,20.0)
#ax.set_ylim(0.0,15.0)
ax.set_title('Tensión (voltaje) del capacitor')
ax.set_xlabel('t [s]')
ax.set_ylabel('Vc [V]')
plt.grid(visible = True, which = 'both', axis = 'both')

fig, bx = plt.subplots(dpi=300)
bx.plot(t,corr)
#bx.set_xlim(0.0,20.0)
#bx.set_ylim(-2.0,7.0)
bx.set_title('Corriente')
bx.set_xlabel('t [s]')
bx.set_ylabel('I [A]')
plt.grid(visible = True, which = 'both', axis = 'both')
plt.show()

#%%

# Ejercicio 3