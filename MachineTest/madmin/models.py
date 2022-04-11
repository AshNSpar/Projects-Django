from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your models here

class MyUserManager(BaseUserManager):
    def create_user(self, email, role, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role, password=None):

        user = self.create_user(
            email,
            password=password,
            role=role
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    options=(("Admin","Admin"),
             ("User","User"))

    role=models.CharField(max_length=40,choices=options,default = "Admin")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role','password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class AddUser(models.Model):

    user_name = models.OneToOneField(MyUser,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=60)
    dob = models.TextField(max_length=9)

    def __str__(self):
        return self.user_name

class AddDevice(models.Model):

    imei_number = models.CharField(max_length=15)
    primary_sim = models.CharField(max_length=10)
    secondary_sim = models.CharField(max_length=10)
    options = (("android", "android"), ("apple", "apple"), ("windows", "windows"))
    firmware_option = models.CharField(max_length=50, choices=options, default="android")

    def __str__(self):
        return self.imei_number