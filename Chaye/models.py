from django.db import models

from django.utils import timezone

# Create your models here.

class Chaivarity(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),

        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),


    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais-db-images/')  #Handle Images
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description=models.TextField(default='')
    Price=models.FloatField(default=0)



    def __str__(self)->str:
        return self.name #to see name description in admin panel






