import gmsh_api
from gmsh_api import gmsh


def test_mesh_3d():
    gmsh.initialize()
    gmsh.model.add("3D_Shell_from_3DPolygon")

    gmsh.option.setNumber("Mesh.RecombineAll", 1)
    gmsh.option.setNumber("Mesh.Algorithm", 5)  # DelQuad
    gmsh.option.setNumber("Mesh.RecombinationAlgorithm", 1)
    lc = 0.2

    # 3D-Polygon-Umriss (z. B. leicht gewölbt)
    polygon_points = [
        (0, 0, 0),
        (1, 0, 0.5),
        (1, 1, 0.2),
        (0, 1, -0.1)
    ]

    # Punkte anlegen
    pt_tags = [gmsh.model.occ.addPoint(x, y, z, lc) for x, y, z in polygon_points]

    # Linienzug (Spline oder Line)
    line_tags = []
    for i in range(len(pt_tags)):
        line_tags.append(
            gmsh.model.occ.addSpline([pt_tags[i], pt_tags[(i + 1) % len(pt_tags)]])
        )

    loop = gmsh.model.occ.addCurveLoop(line_tags)

    # Freiformfläche erzeugen
    surface = gmsh.model.occ.addSurfaceFilling(loop)

    # Zusätzliche 3D-Punkte zur besseren Vernetzung
    extra_points = [
        (0.5, 0.5, 1.7),
        (0.25, 0.25, 0.3)
    ]

    for x, y, z in extra_points:
        pt = gmsh.model.occ.addPoint(x, y, z, lc)
        # Als PhysicalGroup(0) markieren → garantiert im Netz enthalten
        gmsh.model.addPhysicalGroup(0, [pt])

    # Fläche als Physical Surface
    gmsh.model.addPhysicalGroup(2, [surface])

    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(2)

    mesh = gmsh_api.Mesh.from_gmsh(gmsh)
    print(mesh)
    print(mesh.nodes)
    print(mesh.elements)


    assert len(mesh.elements) == 44
    assert len(mesh.nodes) == 59
