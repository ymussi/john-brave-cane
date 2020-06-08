from brave_cane.api import api
from brave_cane.config import config_db
from brave_cane.api.healthcheck.view import ns as healthcheck
from brave_cane.api.partner.view import ns as partner
from flask import Flask, Blueprint
from flask_cors import CORS


def create_app(config_filename=None):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    # app.wsgi_app = CheckUserToken(app.wsgi_app)

    connect_string = config_db()['database_uri']
    app.config['SQLALCHEMY_DATABASE_URI'] = connect_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['RESTPLUS_MASK_SWAGGER'] = False

    blueprint = Blueprint('login', __name__)
    api.init_app(blueprint)
    api.add_namespace(healthcheck, "/healthcheck")
    api.add_namespace(partner, "/partner")
    

    app.register_blueprint(blueprint)

    # plug teardown routines
    app.teardown_appcontext(shutdown_session)
    return app


def shutdown_session(exception=None):
    from brave_cane.database import session
    session.remove()
