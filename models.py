from peewee import (
    BooleanField,
    CharField,
    FixedCharField,
    Model,
    PostgresqlDatabase,
    PrimaryKeyField,
)

db = PostgresqlDatabase(
    'walkerdowntheaisle',
    user='eliotwalker',
    host='localhost',
)


class Attendee(Model):

    class Meta:
        database = db

    id = PrimaryKeyField()
    title = FixedCharField(max_length=4, null=True)
    first_name = CharField()
    last_name = CharField()
    attending = BooleanField()
    submission = CharField()
    comments = CharField(max_length=2048, null=True)

    def __repr__(self):
        return repr(self.__dict__)

    def __str__(self):
        return self.__repr__()


db.create_table(Attendee, safe=True)
