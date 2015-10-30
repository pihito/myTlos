from mongoengine import *

CC_CONST = {"maxLvl" : 2, "maxCoef" : 2}

class Projet (Document) : 
    name = StringField(max_length=50, required=True)
    description = StringField(max_length=500, required=True)
    TlosEstimate = (min_value =0,precision = 1)

class Task(Document) : 
    name = StringField(max_length=50, required=True)
    description = StringField(max_length=500, required=True)
    tlosEstimate = (min_value =0,precision = 1)
    budget = = (min_value =0,precision = 2)
    
class ImplTask(Document) :
    name = StringField(max_length=50, required=True)
    description = StringField(max_length=500, required=True)


class UserApp(Document) : 
    userName = StringField(max_length=30, required=True)
    

class Contributeur (Document) :
    username = ReferenceField(Contributeur)
    lastName = StringField(max_length=30, required=True)
    firstName = StringField(max_length=30, required=True)
    email =  EmailField( required=True)
    trelloAccount = StringField(max_length=30, required=True)
    rizzomaAccount StringField(max_length=30, required=True)
    organisation = StringField(max_length=30)
    photo = StringField(max_length=30, required=True)
    Project = ListField(ReferenceField(Project))
    
class commonCoins (Document): 

    userName = ReferenceField(Contributeur,required=True)
    when = DateeTimeField(required=True)
    startHours = DecimalField(min_value =0,max_value max_value = 24,precision = 1, required=True)
    endHours = DecimalField(min_value =0, max_value = 24,precision = 1,required=True)
    project = ReferenceField(Project)
    task = StringField(max_length=50,required=True )
    taskL1 = StringField(max_length=50)
    taskL2 = StringField(max_length=50)
    implType = StringField(max_length=50,required=True)
    taskComment = StringField(max_length=200)
    gift = DecimalField(min_value =0,precision = 1,required=True)
    coef = DecimalField(min_value =0, max_value = TLOS_CONST.maxCoef,precision = 1,required=True)
    expertLvl = DecimalField(min_value =0, max_value = TLOS_CONST.maxLvl,precision = 1,required=True)
    travelFee = DecimalField(min_value =0,precision = 1)
    BuyFee = DecimalField(min_value =0)
    
    



if __name__ == "__main__" : 
    connect('project1', host='mongodb://localhost/database_name')