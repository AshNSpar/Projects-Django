from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, User)

# from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your models here

class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, role, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,phone, role, password=None):

        user = self.create_user(
            email,
            password=password,
            phone=phone,
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
    phone = models.PositiveIntegerField()

    options=(("Applicant","Applicant"),
             ("HR","HR"))

    role=models.CharField(max_length=40,choices=options,default = "Applicant")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','role','password']

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

class CompanyProfile(models.Model):

    company = models.OneToOneField(MyUser,on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=60)
    company_description = models.TextField(max_length=200)
    logo= models.ImageField(upload_to='logo',null=True)

    def __str__(self):
        return self.company_name

class JobseekerProfile(models.Model):

    user = models.OneToOneField(MyUser,on_delete=models.CASCADE,null=True)
    profile_picture = models.ImageField(upload_to='image',null=True)
    name = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resume',null=True)

    def __str__(self):
        return self.name

class JobModel(models.Model):

    company = models.ForeignKey(CompanyProfile,on_delete=models.CASCADE,null=True)
    post_name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.post_name

class ApplicationModel(models.Model):

    job =models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    job_seeker = models.ForeignKey(JobseekerProfile,on_delete=models.CASCADE,null=True)
    options = (("active","active"),("closed","closed"),("rejected","rejected"),("selected","selected"))
    application_status = models.CharField(max_length=50,choices=options,default="active")