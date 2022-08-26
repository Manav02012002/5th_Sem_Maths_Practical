# MT5P2 Experiment 1 
# Program to calculate the Gradient
# Manav Madan Rawal 20PCM53

from sympy import*
x,y,z = symbols("x,y,z")
def gradient(f):
    a = diff(f,x)
    b = diff(f,y)
    c = diff(f,z)
    print("Gradient is (",a, ")i + (",b,")j + (",c,")k")
f = 2*(x**2)*(y**3)*z
gradient(f)