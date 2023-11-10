from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='media/',blank=True, height_field=None, width_field=None, max_length=100)
    content= models.TextField(max_length=1000)
    slug= models.SlugField(null=True)
    date= models.DateField(blank=True,auto_created=True)


    def __str__(self):
        return f'{self.slug}-{self.date}'


    def get_absolute_url(self):
        return reverse("create", kwargs={"slug": self.slug})



