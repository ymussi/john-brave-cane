from brave_cane.api import api
from brave_cane.config import config_db
from brave_cane.api.healthcheck.view import ns as healthcheck
from brave_cane.api.partner.view import ns as partner
from brave_cane.api.partner.app_graphql import GQLPdv
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_graphql import GraphQLView


def create_app(config_filename=None):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

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
    app.teardown_appcontext(shutdown_session)
    return app

def create_graphql(_app):
    _app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
        "graphql",
        schema=GQLPdv,
        graphiql=True
    ))
    return _app


def shutdown_session(exception=None):
    from brave_cane.database import session
    session.remove()
