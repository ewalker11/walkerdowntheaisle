import os
import urlparse

POSTGRES_URL = urlparse.urlparse(os.getenv(
    'DATABASE_URL',
    'postgres://eliotwalker@localhost:5432/walkerdowntheaisle',
))
