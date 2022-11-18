# {{cookiecutter.project_name}} <!-- omit in toc -->

{{cookiecutter.description}}

# Contents <!-- omit in toc -->

1. [Usage](#usage)
   1. [Setup](#setup)
   2. [Training](#training)
   3. [Evaluation](#evaluation)
   4. [Test](#test)
2. [Development](#development)
   1. [Setup](#setup-1)
3. [Project Organization](#project-organization)

# Usage

## Setup

1. Environment variables.

   ```commandline
   cp .env.example .env
   ```

2. Requirements.

   ```commandline
   pip install -r requirements.txt
   ```

## Training

Training model in commandline.

1. Single setting.

   ```commandline
   python {{ cookiecutter.repo_name }}/scripts/train.py
   ```

2. Run shells

   ```commandline
   python {{ cookiecutter.repo_name }}/shells/train.sh
   ```

## Evaluation

Evaluate model performance.

```commandline
python {{ cookiecutter.repo_name }}/scripts/evaluate.py
```

## Test

Inference single sample.

```commandline
python {{ cookiecutter.repo_name }}/scripts/test.py
```

# Development

## Setup

1. Environment variables.

   ```commandline
   cp .env.example .env
   ```

2. Requirements.

   ```commandline
   pip install -r requirements.txt
   ```

   or

   ```commandline
   pip install -r requirements-dev.txt
   ```

3. Install git hook

   If project use version control, use `pre-commit install` to install git hook.

# Project Organization

```

├── datasets
│   ├── external        <- Data from third party sources.
│   ├── final           <- The final, canonical data sets for modeling.
│   ├── interim         <- Intermediate data that has been transformed.
│   └── raw             <- The original, immutable data dump.
│
├── logs                <- Training logs and serialized models, model predictions, or model summaries.
│
├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
│                          the creator's initials, and a short `-` delimited description, e.g.
│                          `1.0-jqp-initial-data-exploration`.
│
├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures         <- Generated graphics and figures to be used in reporting.
│
├── scripts
│   ├── train.py        <- Scripts to train models
│   │
│   ├── evaluate.py     <- Scripts to evaluate models
│   │
│   └── test.py         <- Scripts to predict single sample via trained models
│
├── shells              <- Base shells. 
│   └── train.sh        <- Shells to run multiple training settings at once.
│
├── {{ cookiecutter.module_name }}  <- Source code for use in this project.
│   │
│   ├── data            <- Scripts to download or generate data
│   │
│   ├── models          <- Scripts to construct model modules and architecture
│   │ 
│   └── utils           <- Scripts to help train/test pipeline
│
├── LICENSE
├── Makefile            <- Makefile with commands.
├── README.md           <- The top-level README for developers using this project.
├── requirements.txt    <- The requirements file for reproducing the analysis environment, e.g.
│                          generated with `pip freeze > requirements.txt`
├── .env.example        <- The example of environment variables. DO NOT ADD .env TO VERSION CONTROL!
├── .flake8             <- Config of flake8.
├── .style.yapf         <- Config of yapf.
├── .pre-commit-config.yaml <- Config of pre-commit.
└── setup.py            <- makes project pip installable (pip install -e .) so {{ cookiecutter.module_name }} can be imported

```

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/daniel-code/pytorch-project-template">pytorch project template</a>. </small></p>
