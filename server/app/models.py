from . import db

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stage = db.Column(db.String(100), nullable=False)
    substages = db.relationship('Substage', backref='stage', lazy=True)
    tools = db.relationship('Tool', backref='stage', lazy=True)

class Substage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    substagename = db.Column(db.String(100), nullable=False)
    substagedesc = db.Column(db.Text)
    exemplar = db.Column(db.Boolean, default=False)
    stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=False)

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    toolName = db.Column(db.String(100), nullable=False)
    toolDesc = db.Column(db.Text)
    toolLink = db.Column(db.String(200))
    toolProvider = db.Column(db.String(100))
    stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=False)

class CycleConnect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Integer, nullable=False)
    end = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50))