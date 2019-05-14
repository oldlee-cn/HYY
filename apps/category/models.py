from datetime import datetime
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name='分类名称')
    desc = models.TextField(max_length=200,verbose_name='描述')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间')


    class Meta:
        verbose_name = '报修分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
