import pytest
import os
from django.core.exceptions import ImproperlyConfigured
from .base import env_var

def test_env_var_func_success():
    var_name = 'HELLO'
    try:
        old_val = os.environ[var_name]
    except:
        old_val = None
    os.environ[var_name] = 'HI'
    curr_val = env_var(var_name)
    if old_val is None:
        del os.environ[var_name]
    else:
        os.environ[var_name] = old_val
    assert curr_val == 'HI'

def test_env_var_func_failure():
    var_name = 'HELLO'
    try:
        old_val = os.environ[var_name]
    except:
        old_val = None
    os.unsetenv(var_name)
    try:
        curr_val = env_var(var_name)
    except ImproperlyConfigured:
        curr_val = None
    if old_val is not None:
        os.environ[var_name] = old_val
    assert curr_val is None

if __name__ == '__main__':
    pytest.main()
