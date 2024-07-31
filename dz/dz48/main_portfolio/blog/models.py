from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()
    pdf = models.FileField(upload_to='skills/pdf/')

    def __str__(self):
        return self.title

