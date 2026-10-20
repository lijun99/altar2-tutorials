# Kinematic slip on a triangular mesh

A synthetic kinematic slip inversion on a curved, slab-like fault meshed with triangles, after the
2016 Pedernales earthquake. The data are bandpassed waveforms, static GPS and an InSAR line of sight,
from stations on land. The same data are inverted two ways, and the results are compared with the
true rupture:

- a linear least squares solution, with [CSI](https://github.com/jolivetr/csi): the slip of each
  patch in each time window, smoothed in space and time, with the hypocenter fixed;
- a Bayesian inversion with AlTar 2: the posterior of the slips, rise times, rupture velocities and
  hypocenter, with their uncertainties.

## The notebooks

1. [step1_csi.ipynb](step1_csi.ipynb): the mesh, the kinematic and static Green's functions (CSI's
   `TriangularPatchesKin` on a pyrocko store), the synthetic rupture and its data, and the least
   squares solution. It writes AlTar's inputs to `input/`.
2. [step2_altar.ipynb](step2_altar.ipynb): the cascaded inversion with AlTar, the static data first,
   then the waveforms, and the posterior against the truth and the least squares solution.

They are stored with their outputs. The results of step 2 come from runs made beforehand with these
configurations.

## The files

- `synthetic.pfg`: AlTar's kinematic model alone, which makes the slip history of the true rupture
  in step 1;
- `static.pfg`: the static inversion;
- `cascaded.pfg`: the cascaded inversion, the static and the kinematic models together.

`input/` and `results/` are made by the notebooks, about 1.5 GB, and are not in the repository.

## Running them

- Step 1 needs CSI (with `TriangularPatchesKin`, and the fix of `buildLaplacian` for triangles with
  a single neighbor), pyrocko, the Green's function store `crust2_2hz_d0` (about 5 GB, from
  `fomosto download kinherd crust2_2hz_d0`) and AlTar 2. It takes a few minutes.
- Step 2 needs AlTar 2 and a GPU. The cascaded inversion took 5.8 hours on one GPU. A cell skips its
  run if the results are in `results/` already.
