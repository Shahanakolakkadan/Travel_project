from django.db import models

# Create your models here.
class place(models.Model):
    Name=models.CharField(max_length=100)
    Img=models.ImageField(upload_to='picture')
    Desc=models.TextField()
    Price=models.IntegerField()
    Offer=models.BooleanField(default=False)