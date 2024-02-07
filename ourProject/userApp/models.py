from django.db import models

# Create your models here.
class User_Model(models.Model):
    users_full_name = models.CharField(max_length=100)
    user_username = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_phone_number = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.users_full_name
    

class Order_Model(models.Model):
    order_full_name = models.CharField(max_length=100)
    order_phone_number = models.CharField(max_length=100)
    order_email = models.EmailField(max_length=100)
    order_address = models.CharField(max_length=200)
    order_address2 = models.CharField(max_length=200)
    order_location= models.CharField(max_length=200)
    order_quantity= models.CharField(max_length=100)
    order_remark = models.TextField(max_length=1000)
    def __str__(self):
        return self.order_full_name
    
    
class Contact_Model(models.Model):
    contact_full_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    contact_message = models.TextField(max_length=1000)
    def __str__(self):
        return self.contact_full_name

