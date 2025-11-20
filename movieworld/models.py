from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    photo = models.FileField(upload_to='media')
    janr = models.CharField(max_length=50)
    year = models.IntegerField()
    rejissyor = models.CharField(max_length=100)
    muddat = models.CharField(max_length=10, help_text="Format: 2h 10m")


    def __str__(self):
        return self.title



