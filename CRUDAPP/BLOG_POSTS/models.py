from django.db import models

# Create your models here.
class StudentModel(models.Model):
    FullName = models.CharField(max_length = 10)
    Id = models.IntegerField(primary_key = True)
    Class  = models.CharField(max_length=10)

    def __str__(self):
        return str(self.Id)