from ckeditor.fields import RichTextField
from django.db import models

class User(models.Model):
    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = '管理员'
    title = models.CharField(max_length=32,verbose_name='标题')
    image = models.ImageField(upload_to='media/manager/image',verbose_name='图片')
    text = RichTextField(verbose_name='内容')
    pingllun = models.CharField(max_length=100,verbose_name='评论')


    def __str__(self):
        return self.title


class pinglun(models.Model):
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    T_pinglun = models.CharField(max_length=32, verbose_name='标题')
    def __str__(self):
        return self.T_pinglun
# Create your models here.
