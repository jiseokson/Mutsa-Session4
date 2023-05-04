from django.db import models

class User(models.Model):
    first_name = models.CharField(verbose_name='first name', max_length=20)
    last_name = models.CharField(verbose_name='last name', max_length=20)
    email = models.CharField(verbose_name='email', max_length=20)
    nickname = models.CharField(verbose_name='nickname', max_length=20)

class Post(models.Model):
    writer = models.ForeignKey(verbose_name='writer', to=User, on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name='title', max_length=20)
    content = models.TextField(verbose_name='content')
    view_count = models.IntegerField(verbose_name='view count')
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)

class Comment(models.Model):
    writer = models.ForeignKey(verbose_name='writer', to=User, on_delete=models.DO_NOTHING)
    comment_on = models.ForeignKey(verbose_name='comment on', to=Post, on_delete=models.DO_NOTHING)
    content = models.TextField(verbose_name='content')
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
