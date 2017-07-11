from django.db import models
from django.utils import timezone

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.email

class Article(models.Model):
    author = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    introduction = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + self.author

class Paragraph(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, default=None)

    def __str__(self):
        return self.text


class Image(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    article = models.ForeignKey(Article)

    def __str__(self):
        return self.description

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    execution_date = models.DateField()

    def __str__(self):
        return self.name
