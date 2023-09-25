from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Burada varsayılan kullanıcı kimliğini (ID) belirtiyoruz.


    def __str__(self):
        return self.name