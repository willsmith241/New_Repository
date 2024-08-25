from django.db import models

# Create your models here.

class Profile(models.Model):
    image=models.ImageField(upload_to='media')
    bio=models.TextField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    title=models.CharField(max_length=200,null=True)
    contact=models.CharField(max_length=200,null=True)
    address=models.TextField(max_length=200,null=True)
    skills=models.CharField(max_length=200,null=True)
    linkdin=models.EmailField(max_length=200,null=True)
    website=models.CharField(max_length=200)

    def __str__(self):
        
        return '{}',format(self.name)


