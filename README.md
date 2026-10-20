# AlTar 2 tutorials

Jupyter notebooks for [AlTar 2](https://github.com/lijun99/altar), a Bayesian framework for
inverse problems, stored with their outputs, so they read as they are on GitHub; AlTar's own
documentation is at [altar2.readthedocs.io](https://altar2.readthedocs.io).

- [An introduction to AlTar/pyre applications: HelloApp](hello/hello.ipynb)
- [An overview of the AlTar framework](linear/linear.ipynb)
- Static slip inversion: a toy model with epistemic uncertainties
  - [Step 1: prepare the input files](intro_cp/toymodel_step1.ipynb)
  - [Step 2: run AlTar2](intro_cp/toymodel_step2.ipynb)
- Kinematic slip on a triangular mesh: a Pedernales-like synthetic, inverted by least squares and by AlTar
  - [Step 1: the synthetic data and a least squares solution, with CSI](kinematic_mesh/step1_csi.ipynb)
  - [Step 2: the Bayesian inversion with AlTar](kinematic_mesh/step2_altar.ipynb)

## Running them

The notebooks need an installed AlTar (see its
[Installation Guide](https://altar2.readthedocs.io/en/latest/guide/Installation.html)), with
`jupyter` and `matplotlib`. Each tutorial is a directory with its notebooks and their inputs; run
them from there, or check them all at once against your AlTar:

```bash
python run.py                 # each tutorial in a scratch copy, the repository is left as it is
python run.py linear          # the notebooks whose paths contain "linear"
python run.py --update        # in place, keeping the new outputs, which GitHub shows
```

The kinematic tutorial needs more: [CSI](https://github.com/jolivetr/csi), pyrocko and a Green's
function store for step 1, and a GPU for step 2, whose inversion takes hours.

## Adding a tutorial

Add a directory with the notebook and its input files, list the notebook above, and store it
with its outputs: `python run.py --update <directory>`.
