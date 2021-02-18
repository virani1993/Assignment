from django.db import models

# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length = 20)
    id = models.IntegerField(primary_key=True)
    Contact = models.IntegerField()
    Address = models.CharField(max_length = 200)


    def __str__(self):
        return self.Name