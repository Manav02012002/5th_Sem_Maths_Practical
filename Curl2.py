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
f1 = y**2 + z**3
f2 = 2*x*y - 5*z
f3 = 3*x*(z**2) - 5*y
curl(f1,f2,f3)