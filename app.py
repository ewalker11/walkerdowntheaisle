import glob
import json
import os

from flask import Flask, render_template
from jinja2 import TemplateNotFound

PAGE_DATA = {}

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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<page>')
def router(page):
    return render_template('{}.html'.format(page), **PAGE_DATA.get(page, {}))


if __name__ == '__main__':
    app.run(debug=True)
