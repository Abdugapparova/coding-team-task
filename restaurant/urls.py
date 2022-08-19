from django.urls import path

from .views import FoodCategoriesListAPIView

urlpatterns = [
    path('foods/', FoodCategoriesListAPIView.as_view()),
]
