from django.db import models
# model for women_ministry 
class Women_ministry(models.Model):
    DATE = models.CharField(max_length=255,blank=False,null=False)
    EVENT = models.TextField()
    VENUE = models.CharField(max_length=255,blank=False,null=False)
#model for youth_ministry 
class Youth_ministry(models.Model):
    DATE = models.CharField(max_length=255,blank=False,null=False)
    EVENT = models.TextField()
    VENUE = models.CharField(max_length=255,blank=False,null=False)




