from django.urls import path
from .views import (
    RecipeListView, 
    RecipeDetailView, 
    # RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    create_recipe
    )
from . import views

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_home'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipe/new/', create_recipe, name='recipe-create'),
    
]