import os
import urlparse

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'password')

MAILER_USERNAME = os.getenv('MAILER_USERNAME')
MAILER_PASSWORD = os.getenv('MAILER_PASSWORD')
MAILER_RECIPIENTS = os.getenv('MAILER_RECIPIENTS').split(',')

POSTGRES_URL = urlparse.urlparse(os.getenv('DATABASE_URL'))
