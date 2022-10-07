from django.db import models


# Create your models here.
# models.CharField
# models.DecimalField(max_digits=3,decimal_places=0)

class Members(models.Model):
  name = models.CharField(max_length=255)
  number = models.CharField(max_length=255) 

    #在admin介面直接顯示資料名稱
  def __str__(self): 
    return self.name