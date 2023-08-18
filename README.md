# Block Stdout
A context manager that blocks the standard output when wrapped around ``print`` statements.

## Installation
```shell
python -m pip install block-stdout
```

## Usage
```python
from blockstdout import BlockPrint


def printer():
    print('I will not be printed')

def tester():
    print('I will be printed')
    with BlockPrint():
        printer()
    print('I will also be printed')

if __name__ == '__main__':
    tester()
```

## Pypi Package
[![pypi-module](https://img.shields.io/badge/Software%20Repository-pypi-1f425f.svg)][pypi]

## License & copyright

&copy; Vignesh Rao

Licensed under the [MIT License][license]

[pypi]: https://pypi.org/project/block-stdout/
[license]: https://github.com/thevickypedia/block-stdout/blob/main/LICENSE
