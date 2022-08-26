# MT5P2 Experiment 1 
# Program to calculate the Curl
# Manav Madan Rawal 20PCM53

from sympy import*
x,y,z = symbols("x,y,z")
def laplacian(f):
    a = diff(f,x,2)
    b = diff(f,y,2)
    c = diff(f,z,2)
    print("Laplacian is ",a+b+c)
f = (x**2) - (y**2) 
laplacian(f)