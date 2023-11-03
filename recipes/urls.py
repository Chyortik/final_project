# from django.contrib import admin
from django.urls import path
from . import views

'app/model_view_type'
'recipes/recipe_detail.html'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes_home'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipes_detail'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipes_create'),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name='recipes_update'),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name='recipes_delete'),
    path('about/', views.about, name='recipes_about'),
]
