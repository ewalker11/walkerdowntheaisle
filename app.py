import glob
import json
import os
import uuid

from flask import Flask, redirect, render_template, request
from jinja2 import TemplateNotFound

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


if __name__ == '__main__':
    app.run(debug=True)
