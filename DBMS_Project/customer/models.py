from django.db import models

# Create your models here.
class CustomerInformation(models.Model):
    Name = models.CharField(max_length=30)
    Customer_id = models.IntegerField()
    Age = models.IntegerField()
    Address = models.CharField(max_length=60)
    Account_number = models.CharField(max_length=20)
    Phone_number = models.IntegerField()

    def __str__(self):
        return self.Name