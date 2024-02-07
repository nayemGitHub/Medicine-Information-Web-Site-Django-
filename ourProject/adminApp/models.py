from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin_Panel(AbstractUser):
    display_name = models.CharField(max_length=100)
    admin_email = models.EmailField(max_length=100)
    admin_phone_number = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)
    admin_confirm_password = models.CharField(max_length=100)
    image =models.ImageField(upload_to='media/prof_pic',default='p.jpg')

    def __str__(self):
        return self.display_name



class Add_Medicine_Info(models.Model):
    medicine_title = models.CharField(max_length= 200)
    medicine_company_name = models.CharField(max_length= 200)
    medicine_price = models.IntegerField()
    medicine_discription = models.TextField(max_length= 700)
    medicine_image = models.ImageField(upload_to="media/medicine_pic/", default="media/medicine_pic/dflt_med_image.jpg")

    def __str__(self):
        return self.medicine_title
    

class Add_Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_article = models.TextField(max_length=20000)
    blog_image = models.ImageField(upload_to="media/blog_pic/", default="media/blog_pic/dflt_blog_image.jpg")

    def __str__(self):
        return self.blog_title

