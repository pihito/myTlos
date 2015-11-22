from datalib import Project, Task
from mongoengine import connect


def createProject():
    p = Project("unittest", "projet de test unitaire")
    p.tasks.append(Task(name="conception", description="concpetion du projet"))
    p.tasks.append(Task(name="implementation", description="implementation du projet"))
    p.tasks.append(Task(name="test", description="test du projet"))
    p.save()

    p = Project("tiers lieu", "projet de test unitaire")
    p.tasks.append(Task(name="conception", description="concpetion du projet"))
    p.tasks.append(Task(name="implementation", description="implementation du projet"))
    p.tasks.append(Task(name="test", description="test du projet"))
    p.save()

    p = Project("maker space", "projet de test unitaire")
    p.tasks.append(Task(name="conception", description="concpetion du projet"))
    p.tasks.append(Task(name="implementation", description="implementation du projet"))
    p.tasks.append(Task(name="test", description="test du projet"))
    p.save()


if __name__ == '__main__':
    connect('tlos_mgt', host="mongodb://appl_tlos:tlos@ds047124.mongolab.com:47124/tlos_mgt")
    Project.drop_collection()
    createProject()
