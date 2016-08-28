from flask.blueprints import Blueprint


blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    return "<html><body><h1>Hello World!</h1></body></html>"
