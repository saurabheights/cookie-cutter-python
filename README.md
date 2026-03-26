# My python cookie-cutter repo.

![CI](https://github.com/saurabheights/cookie-cutter-python/actions/workflows/ci.yml/badge.svg)

This repo supports:

- [x] Package Management using Poetry.
- [x] Docker with two stages - prod and dev.
- [x] Pytest with Doctest and Coverage Report.
- [x] Taskfile for running tasks easily.
- [x] Ruff for code linting.
- [x] Mypy for type checking.
- [x] Pre-commit hooks (ruff lint + format).
- [x] GitHub Actions CI with dependency caching and coverage comments.
- [x] Git repository auto-initialized on generation (initial commit + remote origin set).

# Usage

```bash
pip install cookiecutter
cookiecutter https://github.com/saurabheights/cookie-cutter-python.git
```

You will be prompted for:

| Variable | Default | Description |
|---|---|---|
| `author` | `anonymous` | Your name |
| `email` | `anonymous@gmail.com` | Your email |
| `project_name` | `Python Boilerplate` | Human-readable project name |
| `project_slug` | *(derived from project_name)* | Python package name and directory name |
| `github_host_username` | *(derived from author)* | GitHub username for the remote origin URL |
| `github_repo_slug` | *(derived from project_slug)* | GitHub repository name |
| `project_short_description` | *(boilerplate text)* | One-line description |
| `version` | `0.1.0` | Initial version |
| `license` | `MIT license` | License type |

After generation, the new project directory will have:
- A git repository initialized on the `main` branch
- All files staged and committed as the initial commit
- Remote origin set to `https://github.com/<github_host_username>/<github_repo_slug>.git`

Push your new project with:

```bash
cd <project_slug>
git push -u origin main
```

# Generated Project CI

The generated project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:

- Runs on push/PR to `main` and supports manual dispatch
- Tests against Python 3.9, 3.10, 3.11, 3.12, and 3.13
- Frees disk space on the runner before building
- Caches the Poetry virtualenv (keyed on `poetry.lock`) to speed up subsequent runs
- Posts a coverage comment on pull requests (Python 3.13 run only)
