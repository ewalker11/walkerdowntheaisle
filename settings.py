import os
import urlparse

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'password')

POSTGRES_URL = urlparse.urlparse(os.getenv(
    'DATABASE_URL',
    'postgres://eliotwalker@localhost:5432/walkerdowntheaisle',
))
