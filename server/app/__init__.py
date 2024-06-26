from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='config.Config'):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()
        populate_database()

    return app

# Stage connections
connections = [
    (1, 'Conceptualise', 2, 'Plan'),
    (2, 'Plan', 3, 'Collect'),
    (3, 'Collect', 4, 'Access'),
    (4, 'Access', 5, 'Transform'),
    (5, 'Transform', 1, 'Conceptualise'),
    (3, 'Collect', 6, 'Process'),
    (6, 'Process', 7, 'Analyse'),
    (7, 'Analyse', 8, 'Store'),
    (8, 'Store', 9, 'Publish'),
    (9, 'Publish', 10, 'Preserve'),
    (10, 'Preserve', 11, 'Share'),
    (11, 'Share', 4, 'Access')
]

def populate_database():
    # Create stages
    for stage_id, stage_name, _, _ in connections:
        stage = Stage(id=stage_id, stage=stage_name, description='')
        db.session.add(stage)

    # Create cycle connects
    for source_id, source_name, destination_id, destination_name in connections:
        source_stage = Stage.query.get(source_id)
        destination_stage = Stage.query.get(destination_id)
        cycle_connect = CycleConnect(source_stage=source_stage, destination_stage=destination_stage)
        db.session.add(cycle_connect)

    db.session.commit()

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