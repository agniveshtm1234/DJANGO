from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class CensorInfo(models.Model):
     rating=models.CharField(max_length=8,null=True)
     certified_by=models.CharField(max_length=200,null=True)
     def __str__(self):
          return self.certified_by
     
class mangaka(models.Model):
     name = models.CharField(max_length=100)
     def __str__(self):
          return self.name
     
class studio(models.Model):
     studio_name = models.CharField(max_length=300)
     def __str__(self):
          return self.studio_name
     
class animeinfo(models.Model):
     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
     user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
     title=models.CharField(max_length=250)
     year=models.IntegerField(null=True)     # each of these year,title and summary represents a 
     summary=models.TextField()              # column in RDBMS, infact this method itself is known as ORM - Object Relational Mapping
     BIG3_CH =[('Yes','Yes'),('No','No'),]   
     Big3 = models.CharField(max_length=3,choices=BIG3_CH,default="No") 
     img = models.ImageField(upload_to="images/",null=True)
     censor_details=models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,
                                         related_name='anime', null=True)  #1to1 relation
     manga_of = models.ForeignKey(mangaka,on_delete=models.CASCADE,related_name="authored_stories",null=True)
     studio = models.ManyToManyField(studio,related_name="animated_by")
     def __str__(self):
          return self.title           
      
                                             

     








# (database_value, label_shown_to_user) uses this for radio button values