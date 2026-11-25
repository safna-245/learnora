from django.db import models

from curriculum.models import Course


class Module(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    module_number = models.IntegerField()

    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="modules")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        last_module_object = Module.objects.filter(course=self.course).last()

        if last_module_object:
            self.module_number = last_module_object.module_number + 1
        else:
            self.module_number = 1

        return super().save(*args, **kwargs)
