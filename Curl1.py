# MT5P2 Experiment 1 
# Program to calculate the Curl
# Manav Madan Rawal 20PCM53

from sympy import*
x,y,z = symbols("x,y,z")
def curl(f1,f2,f3):
    a = diff(f3,y)-diff(f2,z)
    b = diff(f1,z)-diff(f3,x)
    c = diff(f2,x)-diff(f1,y)
    print("Curl is (",a, ")i + (",b,")j + (",c,")k")
f1 = 3*y*z
f2 = 2*x**2 
f3 = 5*x*y
curl(f1,f2,f3)