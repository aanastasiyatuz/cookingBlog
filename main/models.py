from django.db import models
from account.models import User

class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return {self.name}

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cooking_time = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipies')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipies')
    created = models.DateTimeField()

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(upload_to='recipies')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipies')