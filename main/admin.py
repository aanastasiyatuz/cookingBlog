from django.contrib import admin
from .models import *


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5

@admin.register(Recipe)
class RecipeAdmiin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]


admin.site.register(Category)
