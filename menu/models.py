from django.db import models
from category.models import Category
import os
import uuid

def generate_menu_item_image_path(instance, filename):
    "Dinamik dosya yükleme yolu oluşturur."
    file_extension = filename.split('.')[-1]
    generated_name = f"{uuid.uuid4()}.{file_extension}"
    return os.path.join('menu', generated_name)
    
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu', null=True, blank=True)

    def __str__(self):
        return self.name
