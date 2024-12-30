<!-- Tip - Pycharm supports easy updating Table of Comment (TOC) using Alt+Enter -->
<!-- TOC -->
* [{{cookiecutter.project_name}}](#cookiecutterproject_name)
  * [Introduction](#introduction)
  * [Setup](#setup)
    * [Developer Dependencies](#developer-dependencies)
  * [License](#license)
<!-- TOC -->

# {{cookiecutter.project_name}}

## Introduction

{{cookiecutter.project_short_description}}

## Setup

### Developer Dependencies

#### Ruff
We use [Taskfile](https://taskfile.dev/) to allow developers to run common tasks. Do enable [autocompletion](https://taskfile.dev/installation/#setup-completions).

```shell
sudo snap install task --classic
echo "source ~/.task.bash" >> ~/.bashrc
```

#### Pre-Commit Hook

You can use pre-commit to trigger `ruff check` and `ruff format` to run on each git commit. 

## License

Distributed under the terms of the `{{cookiecutter.license}}`.

