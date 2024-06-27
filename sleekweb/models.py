# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.

class User(AbstractUser):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Quản lý tài khoản Đăng Nhập"
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('password').blank = False
    AbstractUser._meta.get_field('password').blank = False

   
class Product(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Sản phẩm"
    Name = models.CharField('Tên sản phẩm',max_length=100, null=True, blank=True)
    Price = models.CharField('Giá',max_length=100, null=True, blank=True)
    Promotion_percentage = models.CharField('Phần trăm khuyến mãi',max_length=100, null=True, blank=True)
    Price_Promotion= models.CharField('Giá khuyến mãi',max_length=100, null=True, blank=True)
    Describe = models.TextField('mô tả', null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def __str__(self):
        return str(self.Name)
    
class Image_Product(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Ảnh sản phẩm"
    Belong_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Belong_product_s',null=True, blank=True)
    Avatar = models.ImageField('Ảnh đại diện',upload_to='Product',null=True,blank=True)
    Avatar_url = models.CharField('url_image',max_length=200, null=True, blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True,null=True, blank=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	


   