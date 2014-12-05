import numpy as np
cimport cython
cimport numpy as np

def mandel_np(h, w, xmin=-2, xmax=0.8,
              ymin=-1.4, ymax=1.4, maxit=20):
    """Returns a numpy array image of the Mandelbrot set."""
    x, y = np.ogrid[xmin:xmax:w*1j, ymin:ymax:h*1j]
    c = x+y*1j
    z = c
    output = np.zeros(z.shape, dtype=int) + maxit
    for i in xrange(maxit):
        z = z**2 + c
        diverged = z*z.conj() > 4
        c[diverged] = 0
        z[diverged] = 0
        output[diverged] = i
    return output.T


def mandel_py(h, w, xmin=-2, xmax=0.8,
              ymin=-1.4, ymax=1.4, maxit=20):
    """Returns a numpy array image of the Mandelbrot set."""
    x, y = np.ogrid[xmin:xmax:w*1j, ymin:ymax:h*1j]
    c = x+y*1j
    output = np.zeros(c.shape, dtype=int) + maxit
    for i in range(h):
        for j in range(w):
            z = c[i,j]
            c0 = c[i,j]
            for k in xrange(maxit):
                z = z**2 + c0
                if z*np.conj(z) > 4.0:
                    output[i, j] = k
                    break
    return output.T

def mandel_py1(h, w, xmin=-2, xmax=0.8,
              ymin=-1.4, ymax=1.4, maxit=20):
    """Returns a numpy array image of the Mandelbrot set."""
    x = np.linspace(xmin, xmax, w)
    y = np.linspace(ymin, ymax, h)
    output = np.zeros((w, h), dtype=int) + maxit
    for i in xrange(h):
        for j in xrange(w):
            c0 = complex(x[i], y[j])
            z = c0
            for k in xrange(maxit):
                z = z**2 + c0
                if (z.real*z.real + z.imag*z.imag) > 4.0:
                    output[i, j] = k
                    break
    return output.T


@cython.boundscheck(False)
def mandel_cy(int h, int w, double xmin=-2, double xmax=0.8,
              double ymin=-1.4, double ymax=1.4, int maxit=20):
    """Returns a numpy array image of the Mandelbrot set."""
    cdef np.ndarray[np.complex128_t, ndim=2] c
    cdef np.ndarray[np.int64_t, ndim=2] output
    cdef int i, j, k
    cdef double complex c0, z
    x, y = np.ogrid[xmin:xmax:w*1j, ymin:ymax:h*1j]
    c = x+y*1j
    output = np.zeros((w, h), dtype=np.int64) + maxit
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

