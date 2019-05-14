from datetime import datetime
from django.db import models

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=30,verbose_name='名称')
    management = models.CharField(max_length=10,verbose_name='负责人')
    desc = models.TextField(max_length=200,verbose_name='描述')
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '网格区域'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name