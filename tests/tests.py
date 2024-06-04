from django.test import TestCase

from keyvaluestore.utils import (get_value_for_key, get_value_or_default,
                                 set_key_value)


class KeyValueStoreTests(TestCase):
    def test_get_value_for_missing_key(self):
        self.assertRaises(KeyError, get_value_for_key, "nonexistent")

    def test_get_value_or_default(self):
        default_value = "default123"
        self.assertEqual(
            get_value_or_default("nonexistent", default_value), default_value
        )

    def test_set_value_for_keyt(self):
        key = "cache_key"
        expected_value = "apple123"
        set_key_value(key, expected_value)

        self.assertEqual(get_value_for_key(key), expected_value)
