from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

extensions = [
        Extension("bigfile.pyxbigfile", ["bigfile/pyxbigfile.pyx"],
            include_dirs = ["src/", numpy.get_include()])]

setup(
    name="bigfile", version="0.1.13",
    author="Yu Feng",
    author_email="rainwoodman@gmail.com",
    url="http://github.com/rainwoodman/bigfile",
    description="python binding of BigFile, a peta scale IO format",
    zip_safe = False,
    package_dir = {'bigfile': 'bigfile'},
    install_requires=['cython', 'numpy'],
    packages= ['bigfile', 'bigfile.tests'],
    requires=['numpy'],
    ext_modules = cythonize(extensions)
)
