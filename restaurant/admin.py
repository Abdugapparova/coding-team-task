from django.contrib import admin

from .models import FoodCategory, Food


@admin.register(Food)
class FoodModelAdmin(admin.ModelAdmin):
    ...


@admin.register(FoodCategory)
class FoodCategoryModelAdmin(admin.ModelAdmin):
    ...
