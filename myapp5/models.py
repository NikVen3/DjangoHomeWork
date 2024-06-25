from django.db import models
from django.core.exceptions import ValidationError

def validate_not_negative(value):
    if value < 0:
        raise ValidationError('Значение не может быть отрицательным.')
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    reg_date = models.DateField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_not_negative])
    amount = models.IntegerField()
    image = models.ImageField(null=True)
    added_at = models.DateField(auto_now=True)


class Order(models.Model):
    quantity = models.IntegerField(validators=[validate_not_negative])
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    common_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_not_negative])
    date = models.DateField()
