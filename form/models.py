from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=25)
    ename=models.CharField(max_length=30)
    eemail=models.EmailField()
    eaddress=models.TextField()

    def __str__(self):
        return self.ename