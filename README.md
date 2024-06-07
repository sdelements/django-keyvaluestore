# django-keyvaluestore

django-keyvaluestore implements a very simple database-based key-value store for Django.

This package is a fork and only maintained on an as needed basis since the upstream package is no longer maintained at - https://github.com/vikingco/django-keyvaluestore.

## Install

```bash
pip install git+https://github.com/sdelements/django-keyvaluestore@master
```

## Usage

The interface is straightforward::

```python
    from keyvaluestore import get_value_for_key, set_key_value
    set_key_value('foo', 'bar')
    get_value_for_key('foo')
```
