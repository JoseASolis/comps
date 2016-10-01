from django.db import models
class Classes(models.Model):
    class_name = models.CharField(max_length=100)
    class_teacher = models.CharField(max_length=100)
    data=[]
    data.append(class_name)
    data.append(class_teacher)
    def __str__(self):
        return self.data
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    clas = models.ForeignKey(Classes)
    def __str__(self):
        return self.name
