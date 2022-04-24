from datetime import datetime
from time import time
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    # id is automatically generated
    question_text = models.CharField(max_length=200) # Varchar
    pub_date = models.DateTimeField("date published")

    # 
    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # Restarle al tiempo presente exatamente un día 


class Choice(models.Model):
    # id is automatically generated
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text