import numpy as np

def mandel_py(h, w, maxit=20):
    """Returns a numpy array image of the Mandelbrot set."""
    x, y = np.ogrid[-2:0.8:w*1j, -1.4:1.4:h*1j]
    c = x+y*1j
    output = np.zeros(c.shape, dtype=int) + maxit
    for i in range(h):
        for j in range(w):
            z = c[i,j]
            c0 = c[i,j]
            for k in xrange(maxit):
                z = z**2 + c0
                if z*z.conjugate() > 4.0:
                    output[i, j] = k
                    break
    return output.T

def mandel_np(h, w, maxit=20):
    """Returns a numpy array image of the Mandelbrot set."""
    x, y = np.ogrid[-2:0.8:w*1j, -1.4:1.4:h*1j]
    c = x+y*1j
    z = c
    output = np.zeros(z.shape, dtype=int) + maxit
    # Write your solution here.
