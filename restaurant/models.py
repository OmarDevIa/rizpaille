from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


DELIVERY_STATUS_CHOICES = (
    ('Pending', 'PENDING'),
    ('failed','FAILED'),
    ('completed','COMPLETED')
)

class Meal(models.Model):
    """Name:Model representing a meal.
       description: The description of the meal.
       Author:Omar Ing
    """
    name = models.CharField("nom du repas",max_length=100)
    description = models.TextField("description du repas",blank=True,null=True)
    price = models.DecimalField("Price du repas",max_digits=10, decimal_places=2 )
    image = models.ImageField("Image du repas",upload_to='meal_images',default='meal_images/default_meal.png')
    available = models.BooleanField("Online disponible",default=False)
    stock = models.IntegerField("Stock Count",default=0)

    def __str__(self):
        return f"{self.description}"
    
class OrderTransaction(models.Model):
    """Name:Model representing a order.
       description: The description of the order.
       Author:Omar Ing
    """   
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE) 
    amount = models.DecimalField('Amount Paid($)',max_digits=64, decimal_places=2,default=0)
    status = models.CharField('Delivery Status',max_length=9,choices=DELIVERY_STATUS_CHOICES,default='Pending')
    created_at = models.DateTimeField('Date Created ',default=now)