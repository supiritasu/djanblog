from datetime import timezone
from django.db import models

# Create your models here.
class Blog(models.Model):
   title = models.CharField(max_length=255)
   date = models.DateTimeField()
   img = models.ImageField(upload_to='media/')
   contents = models.TextField(max_length=255)

   

   
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    # image = models.URLField(blank=True, null=True, max_length=500)   
    image = models.CharField(max_length=700, blank=True, null=True) # 画像URLを保存するフィールド
    posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title #dbのタイトルをブログタイトルに変更


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="commnets", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()