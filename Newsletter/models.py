from django.db import models
from Main_Menu.models import category
# Create your models here.



class Subscription(models.Model):
    Subscribe_ID=models.IntegerField(primary_key=True)
    User_email_Address=models.CharField(max_length=100)
    category_ID=models.ForeignKey(category,on_delete=models.CASCADE)


class Newsletter(models.Model):
    Newsletter_ID=models.IntegerField(primary_key=True)
    Newsletter_Type=models.CharField(max_length=100)
    email_list=models.CharField(max_length=100)
    Newsletter_Message=models.CharField(max_length=100)
    Category_ID=models.ForeignKey(category,on_delete=models.PROTECT)