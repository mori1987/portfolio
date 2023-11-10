from django.db import models


class Contact(models.Model):
    name= models.CharField(max_length=50)
    phone_number= models.CharField(max_length=12)
    email= models.EmailField()
    message= models.TextField()

    def __str__(self):
        return self.name