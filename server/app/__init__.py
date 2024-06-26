from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class='config.Config'):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from .config import Config

# db = SQLAlchemy()
# ma = Marshmallow()

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     db.init_app(app)
#     ma.init_app(app)

#     from .routes import main
#     app.register_blueprint(main)

#     return app