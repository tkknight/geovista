import iris
from iris.experimental.ugrid import PARSE_UGRID_ON_LOAD

import geovista as gv

fname = "./qrparm_shared.orog.ugrid.node.nc"
with PARSE_UGRID_ON_LOAD.context():
    cube = iris.load_cube(fname, "surface_altitude")

face_node = cube.mesh.face_node_connectivity
indices = face_node.indices_by_src()
lons, lats = cube.mesh.node_coords

mesh = gv.Transform.from_unstructured(
    lons.points,
    lats.points,
    indices,
    data=cube.data,
    start_index=face_node.start_index,
    name=cube.name(),
)

plotter = gv.GeoPlotter()
plotter.add_coastlines(resolution="50m", color="white", line_width=2)
plotter.add_mesh(mesh, cmap="balance", show_edges=True, edge_color="grey")
plotter.add_axes()
plotter.add_text(
    "Unstructured Cube-Sphere Node Data (N, 4)",
    position="upper_left",
    font_size=10,
    shadow=True,
)
plotter.show()