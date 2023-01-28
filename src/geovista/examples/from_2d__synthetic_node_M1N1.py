#!/usr/bin/env python3
"""
This example demonstrates how to create a mesh from 2-D latitude and longitude
rectilinear cell bounds. The resulting mesh contains quad cells.

The data is synthetically generated and targets the mesh nodes/points.

Note that, Natural Earth coastlines are also rendered.

"""

import numpy as np

import geovista as gv
import geovista.theme  # noqa: F401


def main() -> None:
    # create the 2D spatial coordinates and data
    M, N = 45, 90
    lats = np.linspace(-90, 90, M + 1)
    lons = np.linspace(-180, 180, N + 1)
    mlons, mlats = np.meshgrid(lons, lats, indexing="xy")
    data = np.random.random((M + 1) * (N + 1))

    # create the mesh from the synthetic data
    name = "Synthetic Points"
    mesh = gv.Transform.from_2d(mlons, mlats, data=data, name=name)

    # provide mesh diagnostics via logging
    gv.logger.info(f"{mesh}")

    # plot the mesh
    plotter = gv.GeoPlotter()
    plotter.add_mesh(mesh, clim=(0, 1), cmap="tempo", scalars=name, show_edges=True)
    plotter.add_coastlines()
    plotter.add_axes()
    plotter.add_text(
        "2-D Synthetic Node Data",
        position="upper_left",
        font_size=10,
        shadow=True,
    )
    plotter.show()


if __name__ == "__main__":
    main()
