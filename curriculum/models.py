from django.db import models

from accounts.models import User

class Course(models.Model):

    LEVEL_CHOICES = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    )

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    )

    trainer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="courses")

    title = models.CharField(max_length=200)

    short_description = models.CharField(max_length=300)

    detailed_description = models.TextField()

    thumbnail = models.ImageField(upload_to="course_thumbnails",null=True, blank=True)

    duration = models.IntegerField()

    level = models.CharField(max_length=20,choices=LEVEL_CHOICES,default="beginner")

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="draft")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
