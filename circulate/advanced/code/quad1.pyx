from math import sin
def f(double x):
    return sin(x*x)

def integrate(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0.0
    dx = float(b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx
