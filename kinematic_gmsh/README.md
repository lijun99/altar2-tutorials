# Kinematic slip on a Slab2 slab, meshed by gmsh

The [kinematic_mesh](../kinematic_mesh) synthetic on a fault made the way real ones are: a patch
of the [Slab2](https://doi.org/10.1126/science.aat4723) interface under Ecuador, 160 x 160 km down
dip from its 8 km contour, triangulated by [gmsh](https://gmsh.info) into 132 nearly equilateral
triangles, graded from 17 km at the top to 34 km at the base. The stations, the true rupture and
the noise are kinematic_mesh's. The Bayesian inversion with AlTar 2 samples the slips as a
magnitude and a rake per patch, and is compared with the same inversion sampling the two
components of the slip, as kinematic_mesh does.

## The notebooks

1. [step1_mesh.ipynb](step1_mesh.ipynb): Slab2's depth grid, downloaded once; surface coordinates
   from cross-sections of the slab; the mesh, by gmsh in those coordinates, and kinematic_mesh's
   regular one on the same slab; the Green's functions, the true rupture and its data; and a check
   of the rupture times. It writes AlTar's inputs to `input/`.
2. [step2_altar.ipynb](step2_altar.ipynb): the cascaded inversion with AlTar, the static data first,
   then the waveforms, with polar slips; the posterior against the truth, and against the same
   inversion with independent components.

They are stored with their outputs. The results of step 2 come from runs made beforehand with these
configurations.

## The files

- `synthetic.pfg`: AlTar's kinematic model alone, which makes the slip history of the true rupture
  in step 1;
- `static.pfg`: the static inversion, with polar slips;
- `cascaded.pfg`: the cascaded inversion, with polar slips and the sampler the guide recommends;
- `components/static.pfg`, `components/cascaded.pfg`: the same, with independent components.

`slab2/`, `input/`, `results/` and `components/results/` are about 2 GB, and are not in the
repository.

## Running them

- Step 1 needs CSI (with `TriangularPatchesKin`), gmsh (`pip install gmsh`), pyrocko, the Green's
  function store `crust2_2hz_d0` (about 5 GB, from `fomosto download kinherd crust2_2hz_d0`), AlTar
  2, and fim-python for one comparison. It downloads the Slab2 distribution (140 MB) from
  ScienceBase and keeps South America's depth grid in `slab2/`. It takes a few minutes.
- Step 2 needs AlTar 2 and a GPU. The cascaded inversion took 33 minutes on one GPU. A cell skips
  its run if the results are in `results/` already. The comparison needs the results of the
  configurations in `components/`, run there as in step 2, with a link `input -> ../input`: both
  `sample` runs, and `forward` on the cascaded one into `results/cascaded/forward.h5`.
