from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=200)
    experience = models.IntegerField(default=0)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Skill(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
# Create your models here.
    def __str__(self):
        return self.name
