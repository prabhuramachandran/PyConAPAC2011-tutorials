import time
import mbrt

from enthought.traits.api import (HasTraits, Float, Range, Enum, 
            Array, on_trait_change, Instance)
from enthought.traits.ui.api import (View, Item, Group)

from enthought.chaco.api import ArrayPlotData, Plot, jet
from enthought.enable.component_editor import ComponentEditor


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

    # Plot related traits.
    plotdata = Instance(ArrayPlotData)
    plot = Instance(Plot)

    view = View(Group(
                  Item(name='method'),
                  Item(name='runtime'),
                  Item(name='width'),
                  Item(name='height'),
                  Item(name='xmin'),
                  Item(name='xmax'),
                  Item(name='ymin'),
                  Item(name='ymax'),
                  Item(name='iterations'),
                  Item(name='plot',
                       editor=ComponentEditor(), show_label=False)
                  ),
                  width=600, height=700,
                  resizable=True,
                  title="Mandelbrot set"
                )


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

    def _result_changed(self, res):
        if self.plot is None:
            plotdata = ArrayPlotData(img = res)
            self.plotdata = plotdata
            # Create a Plot and associate it with the PlotData
            plot = Plot(plotdata)
            # Create a line plot in the Plot
            plot.img_plot("img", colormap=jet)
            self.plot = plot
        else:
            self.plotdata.set_data('img', res)


if __name__ == '__main__':
    m = Mandelbrot()
    m.compute() # compute it once.
    m.configure_traits()

