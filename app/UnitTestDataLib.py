import unittest


from datalib import Project, Task
from mongoengine import connect


class TestProjectData(unittest.TestCase):

    """docstring for TestProjectData
"""

    def test_CreateData(self):
        Project.drop_collection()
        p = Project("unittest", "projet de test unitaire")
        p.save()
        print(p.id)
        #t1 = Task("writeData", "ecriture des données")
        #t2 = Task("readData", "ecriture des données")
        #t1.save()
        #t2.save()
        p = Project.objects(name='unittest').first()
        #p.tasks.append(Task("writeData", "ecriture des données"))
        #p.tasks = Task(name="writeData", description="ecriture des données")
        #p.tasks.append()
        p.save()

if __name__ == '__main__':
    connect('tlos_mgt', host="mongodb://appl_tlos:tlos@ds047124.mongolab.com:47124/tlos_mgt")
    unittest.main()
