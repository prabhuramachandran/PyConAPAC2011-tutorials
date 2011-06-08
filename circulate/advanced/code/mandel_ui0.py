import time
import mbrt

from enthought.traits.api import (HasTraits, Float, Range, Enum, 
            Array, on_trait_change)


class Mandelbrot(HasTraits):
    # Traits
    method = Enum('cython', 'python', 'numpy', 
                  desc='the implementation to call')
    width = Range(10, 5000, 512, desc='the width of the image')
    height = Range(10, 5000, 512, desc='the height of the image')
    runtime = Float(0.0, desc='the time for execution')
    iterations = Range(2, 100, 20, desc='maximum number of iterations')

    xmin = Range(-4., 4., -2., desc='the minimum x value')
    xmax = Range(-4., 4., 0.8, desc='the maximum x value')
    ymin = Range(-4., 4., -1.4, desc='the minimum y value')
    ymax = Range(-4., 4., 1.4, desc='the maximum y value')

    # The result of the computation.
    result = Array()

    ##########################################################
    # Methods.
    @on_trait_change('method, width, height, xmin, xmax, ymin, '\
                     'ymax, iterations')
    def compute(self):
        """Calculate the Mandelbrot set based on parameters."""
        methods = {'python': mbrt.mandel_py, 'cython': mbrt.mandel_cy,
                   'numpy': mbrt.mandel_np}
        mandel = methods[self.method]
        t1 = time.time()
        result = mandel(self.height, self.width, self.xmin, self.xmax,
                        self.ymin, self.ymax, self.iterations)
        t2 = time.time()
        self.runtime = t2 - t1
        self.result = result


if __name__ == '__main__':
    m = Mandelbrot()
    m.configure_traits()

