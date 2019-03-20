# gmsh_api

simple package to use gmsh via the original gmsh_api 
(https://gitlab.onelab.info/gmsh/gmsh/blob/master/api/gmsh.py).

Christophe Geuzaine is a hero.

## Usage

    # gmsh_api package with some useful classes 
    import gmsh_api
    # original gmsh-api from gmsh package
    import gmsh_api.gmsh as gmsh
    
    gmsh.initialize()
    
    gmsh.option.setNumber("General.Terminal", 1)
    gmsh.option.setNumber("Mesh.Algorithm", 5) # delquad
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
    #gmsh.write("square.unv")
    
    mesh = gmsh_api.Mesh.from_gmsh(gmsh)
    print(mesh.nodes)
    print(mesh.elements)

## Store mesh properties with pandas dataframes!

### mesh.nodes

          nid         x         y    z
     1      1  0         0           0
     2      2  1         0           0
     3      3  1         1           0
     4      4  0         1           0
     5      5  0.5       0           0
     6      6  1         0.522774    0
     7      7  0.728708  1           0
     8      8  0.472136  1           0
     9      9  0.229485  1           0
    10     10  0         0.786636    0
    11     11  0         0.55051     0
    12     12  0         0.289194    0
    13     13  0.267268  0.304987    0
    14     14  0.703727  0.740444    0
    15     15  0.387068  0.62141     0
    16     16  0.637319  0.370788    0
    17     17  0.189356  0.818467    0
    
### mesh.elements

          pid    elid  type      n_nodes  nodes                 nidxs
     0      1      17  shell4          4  [9L, 17L, 15L, 8L]    [9L, 17L, 15L, 8L]
     1      1      18  shell4          4  [15L, 17L, 10L, 11L]  [15L, 17L, 10L, 11L]
     2      1      19  shell4          4  [10L, 17L, 9L, 4L]    [10L, 17L, 9L, 4L]
     3      1      20  shell4          4  [5L, 16L, 15L, 13L]   [5L, 16L, 15L, 13L]
     4      1      21  shell4          4  [6L, 14L, 15L, 16L]   [6L, 14L, 15L, 16L]
     5      1      22  shell4          4  [6L, 16L, 5L, 2L]     [6L, 16L, 5L, 2L]
     6      1      23  shell4          4  [15L, 14L, 7L, 8L]    [15L, 14L, 7L, 8L]
     7      1      24  shell4          4  [15L, 11L, 12L, 13L]  [15L, 11L, 12L, 13L]
     8      1      25  shell4          4  [5L, 13L, 12L, 1L]    [5L, 13L, 12L, 1L]
     9      1      26  shell4          4  [6L, 3L, 7L, 14L]     [6L, 3L, 7L, 14L]