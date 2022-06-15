from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField('date created')
    Published_date = models.DateTimeField('date published')

    def _str_(self):
        return self.Title + ' | ' + str(self.author)