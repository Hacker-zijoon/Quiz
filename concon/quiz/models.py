from django.db import models


# Create your models here.
class Quiz(models.Model):
    title = models.CharField('제목', max_length = 250)
    image = models.ImageField(
                upload_to = 'quiz/%Y/%m/%d',
                null=True, blank=True,
         )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{pk}'.format(pk=self.id)

class Question(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(
                upload_to = 'question/%Y/%m/%d',
                null=True, blank=True,
         )
    sequence = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}:{}'.format(self.sequence, self.title)

class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.CharField(max_length=250)
    sequence = models.IntegerField(default=0)
    code = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Result(models.Model):
    quiz = models.ForeignKey(Quiz)
    image = models.ImageField(
                upload_to = 'result/%Y/%m/%d',
                null=True, blank=True,
         )
    content = models.TextField()
    code = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class UserScore(models.Model):
    session_key = models.CharField(max_length=32)
    previous = models.OneToOneField('self', null=True)
    quiz = models.ForeignKey(Quiz)
    answer = models.ForeignKey(Answer)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{pk}'.format(pk=self.id)
