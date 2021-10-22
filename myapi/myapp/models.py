from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)

    Answer={
        ("1",option1),
        ("2", option2),
        ("3", option3),
        ("4", option4)

    }

    answer = models.CharField(max_length=100,choices=Answer)

