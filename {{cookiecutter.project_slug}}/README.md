<!-- Tip - Pycharm supports easy updating Table of Comment (TOC) using Alt+Enter -->
<!-- TOC -->
* [{{cookiecutter.project_name}}](#{{ cookiecutter.project_name | replace(" ", "-") }})
  * [Introduction](#introduction)
  * [Setup](#setup)
    * [Developer Dependencies](#developer-dependencies)
      * [Taskfile](#taskfile)
      * [Ruff](#ruff)
      * [Pre-Commit Hook](#pre-commit-hook)
  * [License](#license)
<!-- TOC -->

# {{cookiecutter.project_name}}

## Introduction

{{cookiecutter.project_short_description}}

## Setup

### Developer Dependencies

#### Taskfile

We use [Taskfile](https://taskfile.dev/) to allow developers to run common tasks. Do enable [autocompletion](https://taskfile.dev/installation/#setup-completions).

```shell
sudo snap install task --classic
echo 'eval "$(task --completion bash)"' >> ~/.bashrc
```

#### Ruff

To apply ruff checks and formatting, run:
```shell
task run-lint
```

#### Pre-Commit Hook

You can use pre-commit to trigger `ruff check` and `ruff format` to run on each git commit. 

```shell
pip install pre-commit
pre-commit install
```

## License

Distributed under the terms of the `{{cookiecutter.license}}`.
