from django.db import models

# Create your models here.

class BookStore(models.Model):
    title = models.CharField(max_length=11,verbose_name='书名',)

class Book(models.Model):

    title = models.CharField(max_length=11,verbose_name='书名',unique=True)
    pub = models.CharField(max_length=11,verbose_name='出版社',blank=False)
    price = models.DecimalField(verbose_name='图书定价',max_digits=5,decimal_places=2,default=0.0)
    market_price = models.DecimalField(verbose_name='图书零售价',max_digits=5,decimal_places=2,default=0.0)

    def __str__(self):
        return '<%s>'%(self.title)

class Author(models.Model):
    name = models.CharField(max_length=11,verbose_name='姓名',blank=False)
    age = models.IntegerField(verbose_name='年龄',blank=False,default=1)
    email = models.EmailField(verbose_name='邮箱',max_length=20,blank=True)