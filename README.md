# nphard-generators

This package provides some generators for creating instances of np-hard problems such as maximum-clique-problem or hamiltonian-cycle-problem.
Most of them implement or provide a calculation of the optimal solution for the generated instance.
For more details, see [bachelorarbeit]

## Installation
Ensure you have a valid python installation running, e.g. Python 3.11

### Installing for usage:
`pip install -e .` Installs nphard-generators itself as well as relevant libraries such as numpy, etc.

### Installing for development:
`pip install -e .[dev]` Installs relevant libraries as well as pytest, etc.

### Install from TestPyPi
`pip install --index-url https://test.pypi.org/simple/nphard-generators`

## Packaging

### Build
Generate distribution archives using `python -m build`. (Uses Hatchling as buildbackend)

### Distribute
Upload to TestPyPi using twine:
`python -m twine upload --repository testpypi dist/*`

Upload to PyPi using twine:
`python -m twine upload dist/*`

## Workflow
1. Clone repository
2. Install
3. Edit
4. Test
5. Build
6. Upload

## Docstring
PEP 257; three-double-quote """ format
Docstring for public methods, nontrivial size or non-obvious logic
Content: How to use the method (without providing the actual code); No details

TODO:
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)