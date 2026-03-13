from django.db import models
from django.conf import settings
from questions.models import Question

# Create your models here.

User = settings.AUTH_USER_MODEL

class Vote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    vote_type=models.IntegerField()
