# AlTar 2 tutorials

Jupyter notebooks for [AlTar 2](https://github.com/lijun99/altar), a Bayesian framework for
inverse problems. They are rendered at
[altar2-tutorials.readthedocs.io](https://altar2-tutorials.readthedocs.io); AlTar's own
documentation is at [altar2.readthedocs.io](https://altar2.readthedocs.io).

- [An introduction to AlTar/pyre applications: HelloApp](hello/hello.ipynb)
- [An overview of the AlTar framework](linear/linear.ipynb)
- Static slip inversion: a toy model with epistemic uncertainties
  - [Step 1: prepare the input files](intro_cp/toymodel_step1.ipynb)
  - [Step 2: run AlTar2](intro_cp/toymodel_step2.ipynb)

## Running them

The notebooks need an installed AlTar (see its
[Installation Guide](https://altar2.readthedocs.io/en/latest/guide/Installation.html)), with
`jupyter` and `matplotlib`. Each tutorial is a directory with its notebooks and their inputs; run
them from there, or check them all at once against your AlTar:

```bash
python run.py                 # each tutorial in a scratch copy, the repository is left as it is
python run.py linear          # the notebooks whose paths contain "linear"
python run.py --update        # in place, keeping the new outputs, which the documentation shows
```

## Adding a tutorial

Add a directory with the notebook and its input files, list the notebook in `index.md`, and store
it with its outputs: `python run.py --update <directory>`.
