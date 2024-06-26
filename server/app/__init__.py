from flask import Flask
from .extensions import db, migrate
from .models import Stage, CycleConnect
from .routes import main

def create_app(config_class='config.Config'):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
        populate_database()

    return app

def populate_database():
    # Load the tool information from the provided data
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

    # Create stages and cycle connects
    for source_id, source_name, destination_id, destination_name in connections:
        source_stage = Stage.query.get(source_id)
        if not source_stage:
            source_stage = Stage(id=source_id, stage=source_name, description='')
            db.session.add(source_stage)

        destination_stage = Stage.query.get(destination_id)
        if not destination_stage:
            destination_stage = Stage(id=destination_id, stage=destination_name, description='')
            db.session.add(destination_stage)

        cycle_connect = CycleConnect(source_stage=source_stage, destination_stage=destination_stage)
        db.session.add(cycle_connect)

    db.session.commit()
