import glob
import json
import os
import uuid
from functools import wraps

from flask import Flask, redirect, render_template, request, Response
from jinja2 import TemplateNotFound

import settings
from models import Attendee

PAGE_DATA = {}
GOOGLE_API_KEY = 'AIzaSyD2wKguO9cc4GhsawQS6Ut4Ek9s9s5z5_4'

for filepath in glob.glob('data/*'):
    page = os.path.split(filepath)[1].split('.')[0]
    with open(filepath, 'r') as f:
        PAGE_DATA.update({page: json.load(f)})


app = Flask('walkerdowntheaisle')


@app.errorhandler(404)
def page_not_found(_):
    return render_template('notfound.html'), 404


@app.errorhandler(TemplateNotFound)
def template_not_found(_):
    return render_template('notfound.html'), 404


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\nYou have to login with proper credentials',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == settings.ADMIN_USERNAME and auth.password == settings.ADMIN_PASSWORD:
            return f(*args, **kwargs)
        return authenticate()
    return decorated


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/rsvp', methods=['POST'])
def create_attendees():
    submission = str(uuid.uuid4())
    for i in xrange(int(request.form.get('num_guests'))):
        attending_raw = request.form.get('attending_{}'.format(i))
        attendee = Attendee(
            title=request.form.get('name_title_{}'.format(i)),
            first_name=request.form.get('first_name_{}'.format(i)),
            last_name=request.form.get('last_name_{}'.format(i)),
            attending=(attending_raw == 'yes'),
            submission=submission,
            dinner_option=request.form.get('dinner_option_{}'.format(i))
        )
        if i == 0:
            attendee.comments = request.form.get('comments')
        attendee.save()
    return redirect('ty')


@app.route('/<page>', methods=['GET'])
def router(page):
    return render_template(
        '{}.html'.format(page),
        page_name=page,
        google_api_key=GOOGLE_API_KEY,
        **PAGE_DATA.get(page, {})
    )


@app.route('/admin', methods=['GET'])
@requires_auth
def admin_page():
    attendees = Attendee.select()
    total_attending = 0
    total_not_attending = 0
    for a in attendees:
        if a.attending:
            total_attending += 1
        else:
            total_not_attending += 1

    return render_template(
        'admin.html',
        attendees=attendees,
        total_attending=total_attending,
        total_not_attending=total_not_attending,
    )


if __name__ == '__main__':
    app.run(debug=True)
