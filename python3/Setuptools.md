# `setuptools`

`setuptools` is a builtin package that provides utilities to configure a package

- `setup.py`:
  - Metadata
  - Dependencies
- `setup.cfg`:
  - Package layout
  - Console scripts
  - Third party tools configuration

## Example

```py
import setuptools

setuptools.setup(
  name="scrapper",
  version="0.1.0",
  author="zehuac2",
  author_email="zehuac2@illinois.edu",
  url="https://gitlab.engr.illinois.edu/zehuac2/fa20-cs242-assignment2.git",
  install_requires=[
    "beautifulsoup4==4.9.2",
    "pymongo==3.11.0"
  ])
```

```toml
# Learned from
# https://github.com/pallets/flask/blob/master/setup.cfg

[meta]
name = "scrapper"
version = "0.1.0"
author = "zehuac2"
author_email = "zehuac2@illinois.edu"
url = "https://gitlab.engr.illinois.edu/zehuac2/fa20-cs242-assignment2.git"

[options]
packages = find:
package_dir = = src

[options.packages.find]
where = src

[options.entry_points]
console_scripts =
    scrapper = scrapper.cli:main

[mypy]
mypy_path=stubs/
files=src/**/*.py
```

- `scrapper.cli:main`: the entrypoint for script `scrapper` is at `main`
  function in `scrapper.cli` package
- The above configuration let pip install packages under `src` folder (See more
  at
  [Configuring setup() using setup.cfg files](https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html?highlight=package_dir#options))
