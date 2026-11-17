from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save



class User(AbstractUser):

    phone = models.CharField(max_length=12,unique=True)

    ROLE_CHOICES = (
        ("student","student"),
        ("admin","admin"),
        ("trainer","trainer")
    )

    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")

class StudentProfile(models.Model):

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student")

    qualification = models.CharField(max_length=200,null=True)

    skills = models.CharField(max_length=200,null=True)

    passoutyear = models.CharField(max_length=20,null=True)

    githuburl = models.URLField(null=True)

    linkedurl = models.URLField(null=True)

class TrainerProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    qualification = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    experience = models.CharField(max_length=100)



def create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)


def create_trainer_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "trainer":

        TrainerProfile.objects.create(user=instance)

post_save.connect(create_trainer_profile,sender=User)
