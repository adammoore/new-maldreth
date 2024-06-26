from flask import Blueprint, render_template, jsonify
from .models import Stage, Substage, Tool, CycleConnect
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/lifecycle_data')
def get_lifecycle_data():
    stages = Stage.query.all()
    connections = CycleConnect.query.all()

    stages_data = [
        {
            'id': stage.id,
            'stage': stage.stage,
            'substages': [
                {'id': substage.id, 'substagename': substage.substagename}
                for substage in stage.substages
            ]
        } for stage in stages
    ]

    connections_data = [
        {
            'start': conn.start,
            'end': conn.end,
            'type': conn.type
        } for conn in connections
    ]

    return jsonify({'stages': stages_data, 'connections': connections_data})