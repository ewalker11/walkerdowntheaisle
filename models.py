from datetime import datetime

import pytz
from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    FixedCharField,
    Model,
    PostgresqlDatabase,
    PrimaryKeyField,
)

import settings

db = PostgresqlDatabase(
    settings.POSTGRES_URL.path[1:],
    user=settings.POSTGRES_URL.username,
    password=settings.POSTGRES_URL.password,
    host=settings.POSTGRES_URL.hostname,
    port=settings.POSTGRES_URL.port,
)


class Attendee(Model):

    PACIFIC_TZ = pytz.timezone('America/Los_Angeles')

    class Meta:
        database = db

    id = PrimaryKeyField()
    title = FixedCharField(max_length=4, null=True)
    first_name = CharField()
    last_name = CharField()
    attending = BooleanField()
    submission = CharField()
    comments = CharField(max_length=2048, null=True)
    rsvped_at = DateTimeField(default=datetime.utcnow)
    dinner_option = CharField(null=True)

    @property
    def rsvped_at_local(self):
        if not self.rsvped_at:
            return None

        utc_rsvped_at = self.rsvped_at.replace(tzinfo=pytz.utc)
        return utc_rsvped_at.astimezone(self.PACIFIC_TZ).strftime("%Y-%m-%d %H:%M")

    def __repr__(self):
        return repr(self.__dict__)

    def __str__(self):
        return self.__repr__()


db.create_table(Attendee, safe=True)
