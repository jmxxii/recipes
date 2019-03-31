from django.contrib import admin
from .models import Recipe, Ingredients, Step
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Step)