from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    class Meta:
        verbose_name_plural = "Topic"
    """A TOpics Were user used to write a entry"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        """Returning a string represented of teh model topic"""
        return self.text
class Entry(models.Model):

    """A TOpics Were user used to write a entry"""
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name_plural = "Entry"


    def __str__(self):
        """Returning a string represented of teh model topic"""
        return self.text[:50]+"...."

