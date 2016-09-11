class Attendee(object):

    def __init__(self, title=None, first_name=None, last_name=None, attending=None, submission=None, comments=None):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.attending = attending
        self.submission = submission
        self.comments = comments

    def __repr__(self):
        return repr(self.__dict__)

    def __str__(self):
        return self.__repr__()
