# nphard-generators

This package provides some generators for creating instances of np-hard problems such as maximum-clique-problem or hamiltonian-cycle-problem.
Most of them implement or provide a optimal solution for the generated instance or at least its size.
For more details, see [bachelorarbeit]

## Usage
### Maximum-Clique-Problem
```
from nphard_generators import (
    MCPBrockFactory,
    MCPCFatFactory,
    MCPHamming2Factory,
    MCPSanchisFactory,
    MCPSynA1Factory,
    MCPSynA3Factory
)

MCPSynA1Factory.generate_instance(50, 0.5, 12).to_file("dataset_mcp/syna1.mtx")
MCPCFatFactory.generate_instance(50, 0.3).to_file("dataset_mcp/cfat.mtx")
MCPSanchisFactory.generate_instance(50, 0.5, 12).to_file("dataset_mcp/sanchis.mtx")
MCPHamming2Factory.generate_instance(50).to_file("dataset_mcp/hamming2.mtx")
MCPBrockFactory.generate_instance(50, 0.5, 14, 1).to_file("dataset_mcp/brock.mtx")
MCPSynA3Factory.generate_instance(50, 0.5, 3).to_file("dataset_mcp/syna3.mtx")
```

### Hamiltonian-Cycle-Problem
```
from nphard_generators import HCPPetersenFactory, HCPSynH1Factory, HCPSynH2Factory

HCPSynH1Factory.generate_instance(30, 0.5).to_file("dataset_hcp/synh1.tsp")
HCPSynH2Factory.generate_instance(30, 0.5).to_file("dataset_hcp/synh2.tsp")
HCPPetersenFactory.generate_instance(23*2, 11).to_file("dataset_hcp/petersen_nh.tsp") # non-hamiltonian
HCPPetersenFactory.generate_instance(23*2, 13).to_file("dataset_hcp/petersen_h.tsp") # hamiltonian
```

### Access types
ProblemSolution refers to a whole solution (e.g. size and which nodes), ProblemSimpleSolution only to the size  
`from nphard_generators.types import MCProblemSolution, ...`

## Installation
Ensure you have a valid python installation running, e.g. Python 3.11

### Regular install
`pip install nphard-generators`

### Install from TestPyPi
`pip install --upgrade --index-url https://test.pypi.org/simple/ nphard-generators`

### Installing local for development:
`pip install -e .[dev]` Installs relevant libraries as well as pytest, etc.


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