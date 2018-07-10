from django.db import models
from accounts.models import Profile

# Create your models here.


class Question(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    questionText = models.TextField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.TextField()
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choiceText


class AnswerLog(models.Model):
    profile = models.ForeignKey(Profile, models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)