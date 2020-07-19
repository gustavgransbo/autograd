# gustavgrad
[![Tests](https://github.com/gustavgransbo/gustavgrad/workflows/Tests/badge.svg)](https://github.com/gustavgransbo/gustavgrad/actions?workflow=Tests)
[![codecov](https://codecov.io/gh/gustavgransbo/gustavgrad/branch/master/graph/badge.svg)](https://codecov.io/gh/gustavgransbo/gustavgrad)
[![PyPI](https://img.shields.io/pypi/v/gustavgrad.svg)](https://pypi.org/project/gustavgrad)
[![Python Version](https://img.shields.io/pypi/pyversions/gustavgrad.svg)](https://github.com/gustavgransbo/gustavgrad)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An autograd library built on NumPy, inspired by [Joel Grus's livecoding](https://github.com/joelgrus/autograd/tree/master).

The idea behind gustavgrad is to define a Tensor class, and a set of arithmetic operations on tensors, which we know how to calculate the first order derivative for.
Using the chain-rule, the gradient of the composition of multiple operations can be calculated, since we know how to calculate the first order derivative of the basic operations.
