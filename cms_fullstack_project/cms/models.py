from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (('ADMIN','Admin'),('EDITOR','Editor'),('USER','User'))

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='USER')
    def __str__(self): return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Post(models.Model):
    STATUS_CHOICES=(('DRAFT','Draft'),('PUBLISHED','Published'))
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.ImageField(upload_to='posts/',null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='DRAFT')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
