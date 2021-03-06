from setuptools import setup
from Cython.Distutils import build_ext
from numpy.distutils.extension import Extension as _Extension
import numpy

def Extension(*args, **kw):
    inc = kw.get('include_dirs', [])
    kw['include_dirs'] = inc + [numpy.get_include()]
    return _Extension(*args, **kw)

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("hello", ["hello.pyx"]),
                   Extension("quad0", ["quad0.pyx"]),
                   Extension("quad1", ["quad1.pyx"]),
                   Extension("quad2", ["quad2.pyx"]),
                   Extension("quad3", ["quad3.pyx"]),
                   Extension("quad4", ["quad4.pyx"]),
                   Extension("mandel_cy", ["mandel_cy.pyx"]),
                   Extension("mbrt", ["mbrt.pyx"]),
                  ]
)
