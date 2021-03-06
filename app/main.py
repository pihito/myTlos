from flask import Flask, render_template, request, redirect
from flask.ext.script import Manager
from flask.ext.mongoengine import MongoEngine
from bson import ObjectId
from flask_restful import Resource, Api
from datalib import Project
from flask import jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from FromWtf import ProjectForm

# déclare le serveur flask
app = Flask(__name__)

# set db setting
app.config['MONGODB_SETTINGS'] = {
    'db': 'tlos_mgt',
    'host': "mongodb://appl_tlos:tlos@ds047124.mongolab.com:47124/tlos_mgt"
}

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'beecoinsecret'
WTF_CSRF_SECRET_KEY = 'beecoinsecret'


app.config['DEBUG_TB_ENABLED'] = True
app.config['DEBUG_TB_PANELS'] = ['flask_debugtoolbar.panels.versions.VersionDebugPanel',
                                 'flask_debugtoolbar.panels.timer.TimerDebugPanel',
                                 'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
                                 'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
                                 'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
                                 'flask_debugtoolbar.panels.template.TemplateDebugPanel',
                                 'flask_debugtoolbar.panels.logger.LoggingPanel',
                                 'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
                                 'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
                                 'flask.ext.mongoengine.panels.MongoDebugPanel']

# déclare le plug-in flask-script
manager = Manager(app)
api = Api(app)

# TODO add cible
toolbar = DebugToolbarExtension(app)

db = MongoEngine(app)


@app.route("/")
@app.route("/index")
def landingPage():
    return render_template('index.html')


@app.route("/add_work")
def addwork():
    return render_template('addWork.html')


@app.route("/add_project", methods=('GET', 'POST'))
def addProject():
    projectId = request.args.get('projectId')
    projectResult = None
    pForm = ProjectForm()

    if request.method == 'POST':
        print('****'+pForm.pId.data+'******') 
        if pForm.pId.data is not None and pForm.pId.data != '':
        #Update case
            projectResult = Project.objects(id=pForm.pId.data).first()
            #you need to update the objet and update to escape some cache pbs strange ... 
            projectResult.name = pForm.name.data
            projectResult.description = pForm.description.data
            projectResult.tlosEstimate = pForm.tlosEstimate.data
            projectResult.update(description=pForm.description.data, tlosEstimate=pForm.tlosEstimate.data)

        #create case
        else:
            p = Project(pForm.name.data, 
                        pForm.description.data,
                        pForm.tlosEstimate.data)
            p.save()

    else:
        if projectId is not None:
            projectResult = Project.objects(id=ObjectId(projectId)).first()
            if projectResult.tlosEstimate == None:
                projectResult.tlosEstimate = 0

    return render_template('/addProject.html', form=pForm, p=projectResult)

'''
@app.route("/add_task",metods=('GET','POST'))
def addTask():
    taskName = request.args.get('taskName')
    ProjectName = request.args.get('ProjectName')
    taskResult = None
    tform = TaskForm()

    if request.method == 'POST':
        projectResult = Project.objects(name=tform.pName.data).first()
        if tform.pId is not None:
            
            task = next(t for t in projectResult.tasks if t.name == tName)
            #projectResult.name = pForm.name.data
            projectResult.description = pForm.description.data
            #projectResult.tlosEstimate = pForm.tlosEstimate.data
            projectResult.update(description = pForm.description.data)
    else:
        projectResult = Project.objects(name=ProjectName).first()
        if taskName is not None:
            task = next(t for t in projectResult.tasks if t.name == taskName)
            if task.tlosEstimate == None:
                projectResult.tlosEstimate = 0
            if task.budget == None:
                projectResult.budget = 0

    return render_template('/addTask.html', form=tform, t=task, pName =projectResult.name , pId=projectResult.id)
'''


@app.route("/all_klos")
def allKlos():
    return render_template('all_klos.html')


@app.route("/all_project")
def allProject():
    return render_template('projectTabView.html')


class ApiProject(Resource):

    def post(self):
        projectList = Project.objects()
        data = [{"id":str(p.id),"name": p.name, "description": p.description, "TlosEstimate": str(p.tlosEstimate), "nbrTask": len(p.tasks)} for p in projectList]
        dic = {"current": 1, "rowCount": 10, "rows": data, "total": 1}
        return jsonify(dic)
        # return '{"current": 1,"rowCount": 10,"rows": [{"name": "coucou","description": "123@test.de","Tlos estimate":5}],"total": 1}'

    # def delete(self, projet_name):
    #    abort_if_todo_doesnt_exist(todo_id)
    #    del TODOS[todo_id]
    #    return '', 204

    # def put(self, projet_name):
    #    args = parser.parse_args()
    #    p = Project()
    #    task = {'task': args['task']}
    #    TODOS[todo_id] = task
    #    return task, 201


class NameForm(Form):
    name = StringField("what's your name")
    submit = SubmitField('submit')


@app.route("/test_form", methods=('GET', 'POST'))
def test():
    nameForm = NameForm()
    if nameForm.validate_on_submit():
        return redirect('/success')
    return render_template('test_form.html', form=nameForm)

api.add_resource(ApiProject, '/api/projects')

if __name__ == "__main__":
    # lance le serveur Flask via le plug-in flask-script
    manager.run()
