from math import sin
def f(x):
    return sin(x*x)

def integrate(a, b, N):
    s = 0
    dx = float(b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
