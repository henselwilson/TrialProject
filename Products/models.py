from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=80)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    quantity_available=models.IntegerField(validators=[MaxValueValidator(9999),MinValueValidator(0)])
    class Meta:
        abstract=True

    @property
    def in_stock(self):
        if self.quantity_available==0:
            return False
        return True

class Phone(Product):
    Battery=models.FloatField(max_length=7)
    RAM=models.IntegerField(validators=[MaxValueValidator(64),MinValueValidator(1)])
    Storage=models.IntegerField()

class Orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Phone,on_delete=models.DO_NOTHING)
    quantity=models.IntegerField(validators=[MaxValueValidator(9999),MinValueValidator(0)])


