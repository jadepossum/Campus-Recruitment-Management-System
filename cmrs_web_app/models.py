from django.db import models

# Create your models here.
class Jobs(models.Model):
    Title = models.CharField(("Title"), max_length=50)
    id = models.IntegerField(("ID"), primary_key=True)
    Description = models.CharField(("Desc"),max_length=500, null=True)

    def __str__(self):
        return self.Title

class Users(models.Model):
    name = models.CharField(("Name"), max_length=50)
    id = models.IntegerField(("ID"), primary_key=True)

    def __str__(self):
        return self.name