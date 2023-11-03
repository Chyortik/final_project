from django.core.files.storage import FileSystemStorage
from django.forms.models import BaseModelForm
from django.http import HttpResponse, request
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from . import models

# recipes = [
#     {
#         'author': 'Дима',
#         'title': 'Фрикадельки',
#         'directions': 'Смешайте все ингредиенты',
#         'date_posted': '21 октября 2023 г.'
#     },
#     {
#         'author': 'Дима',
#         'title': 'Яичница',
#         'directions': 'Смешайте все ингредиенты',
#         'date_posted': '16 октября 2023 г.'
#     },
#     {
#         'author': 'Дима',
#         'title': 'Борщ',
#         'directions': 'Смешайте все ингредиенты',
#         'date_posted': '19 октября 2023 г.'
#     },
# ]


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    # return HttpResponse('<h1>Добро пожаловать на сайт рецептов!</h1>')
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/home.html', context)


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'cooking_steps', 'ingredients', 'cooking_time']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'cooking_steps', 'ingredients', 'cooking_time']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes_home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    

def about(request):
    # return HttpResponse('<h1>Приложение для рецептов, позволяющее отслеживать ваши рецепты</h1>')
    return render(request, 'recipes/about.html', {'title': 'страница О нас'})

