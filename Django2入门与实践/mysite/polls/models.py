from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model):
    # 问卷内容
    question_text = models.CharField(max_length=200)
    # 问卷时间
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        """
        判断问卷是否最近(一天内发布的)
        :return:
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 选项内容
    choice_text = models.CharField(max_length=20)
    # 选项得分
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
