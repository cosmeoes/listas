from django.db import models

# Create your models here.
class Download(models.Model):
    url = models.CharField(max_length=1000, primary_key=True)
    title = models.CharField(max_length=200)
    mime = models.CharField(max_length=50)
    filesize = models.IntegerField()
    num_downloads = models.IntegerField(default=1)

    def __str__(self):
        return self.mime+" "+self.title
