from django.db import models

# Create your models here.
class mainmenu(models.Model):
    menuid=models.IntegerField(primary_key=True)
    menuname=models.CharField(max_length=50)
    menutype=models.CharField(max_length=50)
    def __str__(self):
        return self.menuname

class category(models.Model):
    category_id=models.IntegerField(primary_key=True)
    category_name=models.CharField(max_length=50)
    menuname=models.ForeignKey(mainmenu,on_delete=models.CASCADE)
    def __str__(self):
        return self.category_name







