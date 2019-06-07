# -*- coding: utf-8 -*-

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%I:%M:%S')

import os
import sys
import numpy as np
import pandas as pd
import gmsh_api
import gmsh_api.gmsh as gmsh
print("gmsh_api package: v{}".format(gmsh_api.__version__))
print("GMSH_API_VERSION: v{}".format(gmsh.GMSH_API_VERSION))

def test_square():
    gmsh.initialize()

    gmsh.option.setNumber("General.Terminal", 1)
    gmsh.option.setNumber("Mesh.Algorithm", 5)  # delquad
    gmsh.option.setNumber("Mesh.RecombineAll", 1)

    gmsh.model.add("square")
    gmsh.model.geo.addPoint(0, 0, 0, 0.6, 1)
    gmsh.model.geo.addPoint(1, 0, 0, 0.6, 2)
    gmsh.model.geo.addPoint(1, 1, 0, 0.5, 3)
    gmsh.model.geo.addPoint(0, 1, 0, 0.4, 4)
    gmsh.model.geo.addLine(1, 2, 1)
    gmsh.model.geo.addLine(2, 3, 2)
    gmsh.model.geo.addLine(3, 4, 3)
    # try automatic assignement of tag
    line4 = gmsh.model.geo.addLine(4, 1)
    gmsh.model.geo.addCurveLoop([1, 2, 3, line4], 1)
    gmsh.model.geo.addPlaneSurface([1], 6)
    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    # gmsh.write("square.unv")
    mesh = gmsh_api.Mesh.from_gmsh(gmsh)
    print(mesh)
    print(mesh.nodes)
    print(mesh.elements)



    assert len(mesh.elements) == 10
    assert len(mesh.nodes) == 17

