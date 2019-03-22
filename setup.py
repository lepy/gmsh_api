# coding: utf-8

import os
import sys
import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
if sys.version_info[0] < 3:
    with open(path.join(this_directory, 'README.md')) as f:
        long_description = f.read()
else:
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

def extract_version():
    init_py = os.path.join(os.path.dirname(__file__), "gmsh_api", "__init__.py")
    with open(init_py) as init:
        for line in init:
            if line.startswith("__version__"):
                d = {}
                exec (line, d)
                return d["__version__"]
        else:
            raise RuntimeError("Missing line starting with '__version__ =' in %s" % (init_py,))


setup_params = dict(
    name="gmsh_api",
    description=("gmsh - API for a great Finite Element Mesher"),
    version=extract_version(),
    author="Lepy",
    author_email="lepy@mailbox.org",
    url="https://github.com/lepy/gmsh_api",
    license="GPL",
    keywords="fem mesh",

    # long_description=read('README'),

    packages=setuptools.find_packages(exclude=["tests"]),  # , include=[ "./gmsh_api/libgmsh.so"]
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy', 'pandas'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    package_data={'': ['gmsh_api/libgmsh.so']},
    include_package_data=True
)

if __name__ == "__main__":
    setuptools.setup(**setup_params)
