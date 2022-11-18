# Pytorch Project Template <!-- omit in toc -->

_A primary project structure for pytorch work._

# Contents <!-- omit in toc -->

1. [Usage](#usage)
2. [Development](#development)
   1. [Setup](#setup)
   2. [Test](#test)
3. [Acknowledgements](#acknowledgements)

# Usage

1. Install cookiecutter

```commandline
pip install cookiecutter
```

2. Create project based on template
    1. Use GitHub URL directly.
    ```commandline
    cookiecutter https://github.com/daniel-code/pytorch-project-template.git
    ```
    2. Download template, and use it locally.
    ```commandline
    cookiecutter pytorch-project-template
    ```

# Development

## Setup

Install development dependencies.
There are some optional dependencies, like pytorch, pytorch-lightning, mlflow.

```commandline
pip install -r requirements-dev.txt
```

## Test

Some test cases only passed in Linux.

```commandline
cd tests
pytest
```

# Acknowledgements

This repository is based
on [drivendata/cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/)

Difference with the original repository

- add [yapf](https://github.com/google/yapf), python formatter, into project structure
- add pre-commit for git hook
- change folders name that all folder names are unique within the project
- Pytorch wrapper pipeline and mlflow
