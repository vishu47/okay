from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Contacts(models.Model):
    contactName = models.CharField(max_length=30)
    contactEmail = models.CharField(max_length=200)
    contactSubject = models.CharField(max_length=50)
    contactMessage = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.contactName


class Upload_Image(models.Model):
    title = models.CharField(null=True,blank=True,max_length=20)
    image1 = models.ImageField(null=True,blank=True,upload_to='product_img')
    image2 = models.ImageField(null=True,blank=True,upload_to='product_img')
    image3 = models.ImageField(null=True,blank=True,upload_to='product_img')
    image4 = models.ImageField(null=True,blank=True,upload_to='product_img')
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("okay_app:product",kwargs={
            'slug':self.slug
        })    

