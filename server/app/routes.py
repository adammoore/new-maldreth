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

@main_bp.route('/dynamic')
def dynamic_view():
    stages = Stage.query.all()
    connections = CycleConnect.query.all()
    return render_template('dynamic_view.html', stages=stages, connections=connections)

@main_bp.route('/static')
def static_view():
    stages = Stage.query.all()
    connections = CycleConnect.query.all()
    return render_template('static_view.html', stages=stages, connections=connections)

@main_bp.route('/schema')
def schema_view():
    stages = Stage.query.all()
    substages = Substage.query.all()
    tools = Tool.query.all()
    return render_template('schema_view.html', stages=stages, substages=substages, tools=tools)

@main_bp.route('/text')
def text_view():
    return render_template('text_view.html')