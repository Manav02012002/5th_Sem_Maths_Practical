# MT5P2 Experiment 1 
# Program to calculate the Divergence
# Manav Madan Rawal 20PCM53

from sympy import*
x,y,z = symbols("x,y,z")
def divergence(f1,f2,f3):
    print("Divergence is ",f1.diff(x)+f2.diff(y)+f3.diff(z))
f1 = 2*x**2*y
f2 = 3*x
f3 = 4*x*z
divergence(f1,f2,f3)