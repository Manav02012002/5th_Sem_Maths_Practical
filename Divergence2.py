# MT5P2 Experiment 1 
# Program to calculate the Divergence
# Manav Madan Rawal 20PCM53

from sympy import*
x,y,z = symbols("x,y,z")
def divergence(f1,f2,f3):
    print("Divergence is ",f1.diff(x)+f2.diff(y)+f3.diff(z))
f1 = x*y*z
f2 = 3*y*(x**2)
f3 = x*(z**2) - z*(y**2)
divergence(f1,f2,f3)