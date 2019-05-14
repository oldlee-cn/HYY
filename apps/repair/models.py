from datetime import datetime
from django.db import models


from region.models import Region
from category.models import Category
# Create your models here.


class Repair(models.Model):
    SCORE_TYPE = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    name = models.CharField(max_length=100,verbose_name='报修标题')
    username = models.CharField(max_length=15,verbose_name='报修用户')
    userage = models.IntegerField(verbose_name='用户年龄')
    repairregion = models.CharField(max_length=50,verbose_name='报修区域')
    repaircategory = models.CharField(max_length=50,verbose_name='报修分类')
    repairimg = models.ImageField(upload_to="repairimg/",verbose_name='现场图片',null=True,blank=True)
    repaircontent = models.TextField(max_length=500,verbose_name='报修内容')
    worktime = models.IntegerField(verbose_name='处理周期(天)',null=True,blank=True)
    score = models.CharField(choices=SCORE_TYPE,default='5',verbose_name='处理结果评分',max_length=10,null=True,blank=True)
    addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    status = models.CharField(choices=(('1','处理完成'),('2', '未处理')),default=2, max_length=10,verbose_name='是否完成处理',null=True,blank=True)
    class Meta:
        verbose_name = '报修内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

