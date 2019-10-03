from django.db import models

# Create your models here.
class Teams(models.Model):
    imageurl = models.ImageField(upload_to = "Images/")
    Tname = models.CharField(max_length=20)


    class Meta:
        db_table = "TeamsDB"
