from flask import Flask, render_template
from jinja2 import TemplateNotFound


app = Flask('walkerdowntheaisle')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html'), 404


@app.errorhandler(TemplateNotFound)
def template_not_found(e):
    return render_template('notfound.html'), 404


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<page>')
def router(page):
    return render_template('{}.html'.format(page))


if __name__ == '__main__':
    app.run(debug=True)
