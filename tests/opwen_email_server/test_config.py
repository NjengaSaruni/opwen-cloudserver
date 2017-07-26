from re import match
from unittest import TestCase

from opwen_email_server import azure_constants


class ConfigTests(TestCase):
    def test_azure_names_are_valid(self):
        acceptable_config_value = '^[a-z]{3,63}$'
        constants = _get_constants(azure_constants)

        for constant, value in constants:
            if not match(acceptable_config_value, value):
                self.fail('config {} is invalid: {}, should be {}'
                          .format(constant, value, acceptable_config_value))


def _get_constants(container):
    for variable_name in dir(container):
        if variable_name.upper() != variable_name:
            continue
        value = getattr(container, variable_name)
        if not isinstance(value, str):
            continue
        yield variable_name, value
