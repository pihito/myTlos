from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, DecimalField


class ProjectForm(Form):
    pId = StringField("Project Id")
    name = StringField("Project name")
    description = StringField("description")
    tlosEstimate = DecimalField()
    submit = SubmitField('save')


class TaskForm(Form):
    pId = StringField("Project Id")
    pName = StringField("Project name")
    tId = StringField("Project Id")
    tName = StringField("Project name")
    description = StringField("description")
    tlosEstimate = DecimalField()
    budget = DecimalField()
    submit = SubmitField('save')
