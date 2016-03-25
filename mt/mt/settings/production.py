from .base import *

DEBUG = False
ALLOWED_HOSTS += [env_var("HOST_NAME")]
