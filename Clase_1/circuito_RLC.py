#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:03:10 2023

@author: Martín Paredes
"""

"""
NOTAS: 
    1) Correr el código en la consola, no como script
    2) Se recomienda imprimir con la función pprint()
    3) El segundo parámetro de Heaviside debe ser 1, de lo contrario
    lo tomará como 0.5 por defecto
"""

from sympy import *
import numpy as np
from sympy.functions.special.delta_functions import Heaviside

init_printing(use_unicode=True)
t   = symbols('t')
ii  = Function('ii')
v   = Function('v')
ODE1 = Eq(Derivative(ii(t),t),-2.2e3/(10e-6)*ii(t)-1/(10e-6)*v(t)+1/(10e-6)*Heaviside(0,12))
ODE2 = Eq(Derivative(v(t),t), 1/(100e-9)*ii(t))
eq  = (ODE1,ODE2)
res = dsolve(eq,hint='all', ics = {ii(0):0,v(0):0})

# res[0]: corriente
# res[1]: tensión

ten = simplify(res[1])
corr = simplify(res[0])