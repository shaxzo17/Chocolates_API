from django.db import models

class Chocolate(models.Model):
    Type_choice = [
        ('M', 'MILK'),
        ('D' , 'DARK'),
        ('W' , 'WHITE')
    ]
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=55)
    type = models.CharField(max_length=1 , choices=Type_choice)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
