from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150, editable=False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
