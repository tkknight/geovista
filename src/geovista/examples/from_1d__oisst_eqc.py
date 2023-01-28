#!/usr/bin/env python3
"""
This example demonstrates how to create a mesh from 1-D latitude and longitude
rectilinear cell bounds. The resulting mesh contains quad cells.

It uses NOAA/NECI 1/4° Daily Optimum Interpolation Sea Surface Temperature
(OISST) v2.1 Advanced Very High Resolution Radiometer (AVHRR) gridded data
(https://doi.org/10.25921/RE9P-PT57). The data targets the mesh faces/cells.

Note that, a threshold is also applied to remove land NaN cells, and a
NASA Blue Marble texture is rendered as a base layer. The mesh is also
transformed to the Equidistant Cylindrical (Plate Carrée) conformal
cylindrical projection.

"""

import geovista as gv
from geovista.pantry import oisst_avhrr_sst
import geovista.theme  # noqa: F401


def main() -> None:
    # load sample data
    sample = oisst_avhrr_sst()

    # create the mesh from the sample data
    mesh = gv.Transform.from_1d(sample.lons, sample.lats, data=sample.data, clean=False)

    # provide mesh diagnostics via logging
    gv.logger.info(f"{mesh}")

    # remove cells from the mesh with nan values
    mesh = mesh.threshold()

    # plot the mesh
    plotter = gv.GeoPlotter(crs=(projection := "+proj=eqc"))
    sargs = dict(title=f"{sample.name} / {sample.units}", shadow=True)
    plotter.add_mesh(mesh, scalar_bar_args=sargs)
    plotter.add_base_layer(texture=gv.blue_marble())
    plotter.add_axes()
    plotter.add_text(
        f"NOAA/NCEI OISST AVHRR ({projection})",
        position="upper_left",
        font_size=10,
        shadow=True,
    )
    plotter.view_xy()
    plotter.camera.zoom(1.5)
    plotter.show()


if __name__ == "__main__":
    main()
