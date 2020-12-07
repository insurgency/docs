## Development

### Install

```shell script
$ pipenv install --dev -e ./
```

## Usage

### Installation

```shell script
$ pipenv install --dev git+https://github.com/insurgency/docs.git#egg=documentation
```

### `Pipfile`

```toml
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
# ...
documentation = {git = "https://github.com/insurgency/docs.git"}
# ...

[packages]
# ...
```

### `docs/conf.py`

```python
# noinspection PyUnresolvedReferences,PyPackageRequirements
from documentation import *

# Override general settings...

project = ...

...
```

### Building

```shell script
$ sphinx-autobuild ./docs/ ./docs/_build/html/
```
