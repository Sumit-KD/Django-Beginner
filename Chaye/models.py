from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

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


    ##Talking about Models:
    #a.ONE-TO-MANY-->u just give foreign key to represent that table/relation

class ChaiReviews(models.Model):
         chai=models.ForeignKey(Chaivarity, on_delete=models.CASCADE ,related_name='chai_reviews')
         user=models.ForeignKey(User ,on_delete=models.CASCADE)
         rating=models.IntegerField(default=0)
         comment=models.TextField(default='')
         date_added=models.DateTimeField(default=timezone.now)
         def __str__(self):
          return f'{self.user.username} reviews for {self.chai.name} by {self.chai.name}'

      #b.MANY-TO-MANY--> U can use ManyToManyField() to interact with any of the relation & vice versa
class Store(models.Model):
        name=models.CharField(max_length=100)
        location=models.CharField(max_length=100)
        chai_varieties=models.ManyToManyField(Chaivarity,related_name='Stores')

        def __str__(self):
            return self.name


    #c.One to One---> for one unique thing is for other it's related unique field

class Certificate(models.Model):
        chai=models.OneToOneField(Chaivarity,on_delete=models.CASCADE,related_name='certificate')
        certificate_no=models.CharField(max_length=100)
        issue_date=models.DateTimeField(default=timezone.now)
        valid_untill=models.DateTimeField()

        def __str__(self):
          return f'Certificate for {self.name.chai}'










