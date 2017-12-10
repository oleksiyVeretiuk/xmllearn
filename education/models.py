from django.contrib.auth.models import User
from django.db import models


class Theme(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    theme = models.ForeignKey(Theme, related_name='articles')
    code_samples = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    content = models.TextField()
    theme = models.ForeignKey(Theme, related_name='questions')
    code_samples = models.TextField(blank=True)

    def __str__(self):
        return self.content


class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question, related_name='answers')
    correct = models.BooleanField()

    def __str__(self):
        return self.content


class UserResult(models.Model):
    user = models.ForeignKey(User, related_name='results')
    theme = models.ForeignKey(Theme)


class UserAnswer(models.Model):
    result = models.ForeignKey(UserResult, related_name='answers')
    answer = models.ForeignKey(Answer)
    question = models.ForeignKey(Question)
