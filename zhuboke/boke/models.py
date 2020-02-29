from ckeditor.fields import RichTextField
from django.db import models
#分类
class Category(models.Model):
    cname = models.CharField(max_length=30,unique=True)

    class Meta:
        db_table = 't_category'

    def __unicode__(self):
        return u'Category:%s'% self.cname

#标签
class Tag(models.Model):
    Tname = models.CharField(max_length=30,unique=True)

    class Meta:
        db_table = 't_Tag'

    def __unicode__(self):

        return u'Tag:%s' % self.Tname

#数据
class Post(models.Model):
    title = models.CharField(max_length=250,unique=True)#标题
    desc = RichTextField()
    countent = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_Post'

    def __unicode__(self):

        return u'Post:%s'% self.title



# Create your models here.

