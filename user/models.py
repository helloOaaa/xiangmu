from django.db import models

# Create your models here.

class User(models.Model):
    SEX = (
        ('male','man'),
        ('female','woman')
    )
    LOCATION = (
        ('SH','Shanghai'),
        ('BJ','Beijing'),
        ('HN','Henan')
    )
    phonenum = models.CharField(max_length=16,unique=True,db_index=True,verbose_name='Phone_num')
    nickname = models.CharField(max_length=32,verbose_name='Nick_name')
    sex = models.CharField(max_length=8,choices=SEX,verbose_name='Sex')
    birthday = models.DateField(verbose_name='Birthday')
    avatar = models.CharField(max_length=256,verbose_name='Avatar')
    location = models.Field(max_length=64,choices=LOCATION,verbose_name='Location')
