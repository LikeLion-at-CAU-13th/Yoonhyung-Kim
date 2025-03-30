from django.db import models
from posts.models import Post

# Create your models here.

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Comment (BaseModel):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.CharField(max_length=15)
    content = models.TextField()

    def __str__(self):
        return "Written by : " + self.author
    

    

