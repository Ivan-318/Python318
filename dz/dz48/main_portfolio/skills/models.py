from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='skills/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

