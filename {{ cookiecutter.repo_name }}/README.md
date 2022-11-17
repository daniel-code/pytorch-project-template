# {{cookiecutter.project_name}} <!-- omit in toc -->

{{cookiecutter.description}}

# Contents <!-- omit in toc -->

- [Project Organization](#project-organization)

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
