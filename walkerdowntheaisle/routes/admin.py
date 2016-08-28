from flask import request, render_template, redirect, url_for
from flask.blueprints import Blueprint

from walkerdowntheaisle.models.person import Person

blueprint = Blueprint('admin', __name__, template_folder='../templates/admin')


@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/people', methods=['GET', 'POST'])
def people():
    if request.method == 'GET':
        return get_people()
    return create_person()


@blueprint.route('/person/<name>')
def person(name):
    person_ = Person(name=name)
    return render_template('person.html', person=person_)


def get_people():
    return render_template('people.html', people=[])


def create_person():
    return redirect(url_for('admin.person', name=request.form['name']))
