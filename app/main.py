from flask import Flask,render_template,request
from flask.ext.script import Manager

#déclare le serveur flask
app = Flask(__name__)
#déclare le plug-in flask-script 
manager = Manager( app)


#on crée la nouvelle route et on la lie à fonction Hello
@app.route("/")
@app.route("/index")
def landingPage():
    return render_template('index.html')

@app.route("/add_work")
def addwork():
    return render_template('addWork.html')

@app.route("/all_klos")
def allwork():
    return render_template('all_klos.html')

if __name__ == "__main__":
#lance le serveur Flask via le plug-in flask-script
    manager.run()