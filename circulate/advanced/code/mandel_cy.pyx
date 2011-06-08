cimport cython
import numpy as np
cimport numpy as np

@cython.boundscheck(False)
def mandel_cy(int h, int w, int maxit=20):
    """Returns a numpy array image of the Mandelbrot set."""
    cdef np.ndarray[np.complex128_t, ndim=2] c
    cdef np.ndarray[np.int64_t, ndim=2] output
    cdef int i, j, k
    cdef double complex c0, z
    x, y = np.ogrid[-2:0.8:w*1j, -1.4:1.4:h*1j]
    c = x+y*1j
    output = np.zeros((w, h), dtype=int) + maxit
    for i in range(h):
        for j in range(w):
            z = c[i,j]
            c0 = c[i,j]
            for k in xrange(maxit):
                z = z**2 + c0
                if (z*z.conjugate()).real > 4.0:
                    output[i, j] = k
                    break
    return output.T


