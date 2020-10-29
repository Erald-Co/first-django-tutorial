import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
# CharField, DateTimeField etc tells Django what type of data each field holds.
# question_text, pub_date are field's name, machine friendly format.
# --- database will use it as the column name.
# Model code made Django able to create a database schema and create database-access API
# --- for accessing Question and Choice
# "__str__" important buat penjelasan

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'


datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
