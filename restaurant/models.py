from django.db import models

# Create your models here.

class Booking(models.Model):
  name = models.CharField(max_length=255)
  no_of_guests = models.IntegerField()
  bookingdate = models.DateField()
  
  def __str__(self) -> str:
    return self.name


class MenuItem(models.Model):
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.SmallIntegerField()
  
  
  def __str__(self) -> str:
    return f'{self.title} : {str(self.price)}'
  
  def get_item(self):
    return f'{self.title} : {str(self.price)}'