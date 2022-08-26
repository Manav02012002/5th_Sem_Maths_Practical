# MT5P1 Experiment 1 
# Program to calculate Fourier Series
# Manav Madan Rawal 20PCM53

from sympy import*
x = Symbol('x')
s = fourier_series(x**2,(x,-pi,pi))
k = s.truncate(n=4)
print("The Fourier Series Expansion of ", x**2, "is f(x) = ",k," ...")