from django.db import models

# Create your models here.
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     first_name = models.TextField()
#     email = models.EmailField()


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_text = models.TextField()
    publihed_at = models.DateTimeField()
    post_id = models.ForeignKey(Post)

