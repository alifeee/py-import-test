> [!CAUTION]
> MOVED! see <https://git.alifeee.net/py-import-test/about/>
# Python Import Test

Why can one not use [astropy] like this?

```python
import astropy

astropy.cosmology...
```

You have to do this

```python
import astropy.cosmology

astropy.cosmology...
```

## Monkeys

This repository aims to replicate the structure of [astropy] with monkeys.

See [./importer.py](./importer.py)

[astropy]: https://github.com/astropy/astropy
