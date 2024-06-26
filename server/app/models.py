from .app import db

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stage = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    substages = db.relationship('Substage', backref='stage', lazy=True)
    tools = db.relationship('Tool', backref='stage', lazy=True)
    connections = db.relationship('CycleConnect', backref='source_stage', lazy='dynamic', foreign_keys='CycleConnect.source_stage_id')
    connected_stages = db.relationship('CycleConnect', backref='destination_stage', lazy='dynamic', foreign_keys='CycleConnect.destination_stage_id')

    def __repr__(self):
        return f"<Stage(stage='{self.stage}', description='{self.description}')>"

class CycleConnect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=False)
    destination_stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=False)

    def __repr__(self):
        return f"<CycleConnect(source='{self.source_stage.stage}', destination='{self.destination_stage.stage}')>"

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