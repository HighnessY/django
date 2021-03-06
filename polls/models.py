from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.


class Question(models.Model):
    question_test = models.CharField('问题内容', max_length=200)
    pub_date = models.DateField('发布时间')

    def __str__(self):
        return self.question_test

    def was_published_recntly(self):
        if self.pub_date >= timezone.now() - timedelta(days=1):
            return True
        else:
            return False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项内容', max_length=200)
    votes = models.IntegerField('投票数', default=0)

    def __str__(self):
        return self.choice_text

"""
类被翻译为sql执行
create table question if not exists(
    id int primary key increase,
    question_text char(200) comment "问题内容"
    pub_data datetime comment "发布时间"
)

create table choice if not exists(
    id int primary key increase,
    choice_text char(200) comment "选项内容"
    votes char(200)
)
"""


# django自带orm框架，用法类似sqlalchemy
# 自定义的类要继承orm框架中的Model类，这样才能把类和数据库连接起来。
