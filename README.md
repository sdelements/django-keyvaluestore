# django-keyvaluestorage

django-keyvaluestorage implements a very simple database-based key-value store for Django.

Published on PyPi as https://pypi.org/project/django-keyvaluestorage/ due to conflicting package name.

## Usage

The interface is straightforward::

```python
    from keyvaluestore import get_value_for_key, set_key_value
    set_key_value('foo', 'bar')
    get_value_for_key('foo')
```
