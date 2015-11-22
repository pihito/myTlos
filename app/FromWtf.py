from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, DecimalField


class ProjectForm(Form):
    pId = StringField("Project Id")
    name = StringField("Project name")
    description = StringField("description")
    tlosEstimate = DecimalField()
    submit = SubmitField('save')
