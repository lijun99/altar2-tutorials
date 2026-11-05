# Kinematic slip on a graded triangular mesh

The [kinematic_mesh](../kinematic_mesh) example on a mesh made the way real fault meshes are: a
triangulation by [gmsh](https://gmsh.info) of nearly equilateral triangles, graded from 17 km at the
trench to 34 km at depth, instead of a grid of rectangles cut in two. The slab, the stations, the
true rupture and the noise are kinematic_mesh's, so the Bayesian inversion with AlTar 2 can be
compared on both meshes.

## The notebooks

1. [step1_mesh.ipynb](step1_mesh.ipynb): the mesh, by gmsh in the surface coordinates of the slab;
   the Green's functions, the true rupture and its data; and a check of the rupture times on the
   graded mesh, against the exact ones and by refinement. It writes AlTar's inputs to `input/`.
2. [step2_altar.ipynb](step2_altar.ipynb): the cascaded inversion with AlTar, the static data first,
   then the waveforms, and the posterior against the truth and against the same inversion on the
   regular mesh.

They are stored with their outputs. The results of step 2 come from runs made beforehand with these
configurations; those of the regular mesh, in `regular/`, from the same sampler on kinematic_mesh's
inputs.

## The files

- `synthetic.pfg`: AlTar's kinematic model alone, which makes the slip history of the true rupture
  in step 1;
- `static.pfg`: the static inversion;
- `cascaded.pfg`: the cascaded inversion, with the sampler the guide recommends.

`input/`, `results/` and `regular/` are about 5 GB, and are not in the repository.

## Running them

- Step 1 needs CSI (with `TriangularPatchesKin`), gmsh (`pip install gmsh`), pyrocko, the Green's
  function store `crust2_2hz_d0` (about 5 GB, from `fomosto download kinherd crust2_2hz_d0`), AlTar
  2, and fim-python for one comparison. It takes a few minutes.
- Step 2 needs AlTar 2 and a GPU. The cascaded inversion took 52 minutes on one GPU. A cell skips
  its run if the results are in `results/` already. The comparison with the regular mesh needs its
  results in `regular/`: kinematic_mesh's `input/mesh.h5` and `input/synthetic.h5`, and the results
  of its inputs with this example's `static.pfg` and `cascaded.pfg` (with `patches = 128`).
