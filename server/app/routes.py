from flask import Blueprint, render_template, jsonify
from flask import request, redirect, url_for

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
            'source_stage_id': conn.source_stage_id,
            'destination_stage_id': conn.destination_stage_id,
        } for conn in connections
    ]

    return jsonify({'stages': stages_data, 'connections': connections_data})

@main.route('/dynamic')
def dynamic_view():
    stages = Stage.query.all()
    connections = CycleConnect.query.all()
    return render_template('dynamic_view.html', stages=stages, connections=connections)

@main.route('/static')
def static_view():
    stages = Stage.query.all()
    connections = CycleConnect.query.all()
    return render_template('static_view.html', stages=stages, connections=connections)

@main.route('/schema')
def schema_view():
    stages = Stage.query.all()
    substages = Substage.query.all()
    tools = Tool.query.all()
    return render_template('schema_view.html', stages=stages, substages=substages, tools=tools)

@main.route('/text')
def text_view():
    return render_template('text_view.html')


@main.route('/tools', methods=['GET', 'POST'])
def manage_tools():
    if request.method == 'POST':
        tool = Tool(
            name=request.form['name'],
            description=request.form['description'],
            stage_id=request.form['stage_id']
        )
        db.session.add(tool)
        db.session.commit()
        return redirect(url_for('main.manage_tools'))

    tools = Tool.query.all()
    stages = Stage.query.all()
    return render_template('tools_management.html', tools=tools, stages=stages)
