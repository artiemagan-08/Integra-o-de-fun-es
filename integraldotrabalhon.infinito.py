#Escrito por ABAM para calcular a integral da função retornada por "integral(x)".

import mpmath
from mpmath import mp, sqrt, quad, inf, nstr

mp.dps = 80

def integral(x):
	num = 3*x**2 + d**2
	den = (x**2 + d**2)**3
	return mp.sqrt(mp.mpf(num)/mp.mpf(den))

W = mp.quad(integral, [0, mp.inf])

mp.nprint(W,16)
