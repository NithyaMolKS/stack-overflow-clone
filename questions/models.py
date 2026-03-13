from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    description =models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

