from flask import Flask

from walkerdowntheaisle.routes.admin import blueprint as admin_blueprint
from walkerdowntheaisle.routes.index import blueprint as index_blueprint

app = Flask('walkerdowntheaisle')

app.register_blueprint(index_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
