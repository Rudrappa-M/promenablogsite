from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.


class Categories(models.TextChoices):
    category_id = models.IntegerField(primary_key=True)
    WORLD = 'world'
    TECHNOLOGY = 'technology'
    ENVIRONMENT = 'environment'
    SCIENCE = 'science'
    PROGRAMMING = 'programming'
    TRAVEL = 'travel'


class BlogPost(models.Model):
    Blog_id = models.IntegerField(primary_key=True, default=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WORLD)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=3)
    content = RichTextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    # Author_id = models.ForeignKey('', related_name='comments', on_delete=models.CASCADE)
    # Category_id = models.ForeignKey('', related_name='comments', on_delete=models.CASCADE)


class CommentModel(models.Model):
    Comment_id = models.IntegerField(primary_key=True)
    Blog_id = models.ForeignKey('BlogPost', related_name='blog', on_delete=models.CASCADE)
    Comment = models.TextField(max_length=100)


class ReplyModel(models.Model):
    Reply_id = models.IntegerField(primary_key=True)
    Blog_id = models.ForeignKey('BlogPost', related_name='blogModel', on_delete=models.CASCADE)
    Comment_id = models.ForeignKey('CommentModel', related_name='comment', on_delete=models.CASCADE)
    Reply_message = models.TextField(max_length=100)

