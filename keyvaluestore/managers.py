from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class KeyValueStoreManager(models.Manager):
    def get_value_for_key(self, key):
        from keyvaluestore.utils import get_cache_key

        cached_key = get_cache_key(key)
        cached = cache.get(cached_key)

        if cached is None:
            try:
                obj = self.get(key=key)
                cache.set(cached_key, obj.value)

                return obj.value
            except ObjectDoesNotExist:
                raise KeyError("The request key '%s' could not be found." % key)
        else:
            return cached
