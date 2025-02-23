from django.db import models

# Create your models here.

class Reports(models.Model):
    email = models.EmailField(max_length=254,blank=False,null=False)
    name = models.CharField(max_length=254,blank=False,null=False)
    mensagem = models.TextField(blank=False, null=False)
    