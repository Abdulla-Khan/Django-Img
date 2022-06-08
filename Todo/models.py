from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=10, null=True)
    rent = models.CharField(max_length=10, null=True)
    photo = models.ImageField(upload_to='pics', null=True)

    def __str___(self):
        return self.title
