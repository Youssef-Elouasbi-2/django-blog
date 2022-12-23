from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.bio + self.location + str(self.birthdate)

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1500)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text + self.title + str(self.author) + str(self.createddate)