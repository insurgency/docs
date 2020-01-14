## Install

```
$ pipenv install --dev -e git+https://github.com/insurgency/docs.git#egg=documentation
```

### `Pipfile`

```toml
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
# ...
documentation = {editable = true,git = "https://github.com/insurgency/docs.git"}
# ...

[packages]
# ...

[requires]
python_version = "..."
```

### `docs/conf.py`

```python
# noinspection PyUnresolvedReferences,PyPackageRequirements
from conf import *

# Override general settings...

project = ...
...
```
