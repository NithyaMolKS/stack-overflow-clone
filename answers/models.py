from django.db import models
from django.conf import settings
from questions.models import Question
# Create your models here.

user = settings.AUTH_USER_MODEL

class answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    author = models.ForeignKey(user,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
