cdef extern from "math.h":
    double sin(double)

cdef class Function:
    cpdef double eval(self, double x) except *:
        return 0

cdef class SinOfSquareFunction(Function):
    cpdef double eval(self, double x) except *:
        return sin(x*x)

def integrate(Function f, double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0.0
    dx = float(b-a)/N
    for i in range(N):
        s += f.eval(a+i*dx)
    return s * dx
