from __future__ import unicode_literals

from django.db import models

# Create your models here
class Articles(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='skate.jpg',blank=True)
    img0 = models.ImageField(default='default.png', blank=True)
    img0cap = models.CharField(max_length=500, default='caption')
    img1 = models.ImageField(default = 'default.png',blank=True)
    img1cap = models.CharField(max_length=500, default='caption')
    img2 = models.ImageField(default='default.png', blank=True)
    img2cap = models.CharField(max_length=500,default='caption')
    img3 = models.ImageField(default='default.png', blank=True)
    img3cap = models.CharField(max_length=500,default='caption')
    img4 = models.ImageField(default='default.png', blank=True)
    img4cap = models.CharField(max_length=500,default='caption')
    img5 = models.ImageField(default='default.png', blank=True)
    img5cap = models.CharField(max_length=500,default='caption')
    img6 = models.ImageField(default='default.png', blank=True)
    img6cap = models.CharField(max_length=500,default='caption')
    img7 = models.ImageField(default='default.png', blank=True)
    img7cap = models.CharField(max_length=500,default='caption')
    img8 = models.ImageField(default='default.png', blank=True)
    img8cap = models.CharField(max_length=500,default='caption')
    img9 = models.ImageField(default='default.png', blank=True)
    img9cap = models.CharField(max_length=500,default='caption')



    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]

    





