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


#%%

# Ejercicio 3