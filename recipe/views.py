from django.shortcuts import render, redirect
from .models import Recipe, Ingredients, Step
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RecipeCreateForm, IngredientsCreateForm, StepCreateForm
from django.contrib import messages

# Create your views here.

def home(request):
    all_recipes = {
        'recipes': Recipe.objects.all()
    }
    print("This is Home")
    return render(request, 'recipe/home.html', all_recipes)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']


class RecipeDetailView(DetailView):
    model = Recipe

def get_recipe_details(request):
    print('REQUEST&&&&&======', request)
    return render(request, 'recipe/recipe_detail.html')

def create_recipe(request):
    if request.method == "POST":
        c_recipe = RecipeCreateForm(request.POST)
        c_ingredients = IngredientsCreateForm(request.POST)
        c_steps = StepCreateForm(request.POST)
        if c_recipe.is_valid() and c_ingredients.is_valid():
            c_recipe.instance.author = request.user
            c_ingredients.instance.recipe = c_recipe.instance
            c_recipe.save()
            c_ingredients.save()
            c_steps.save()
            messages.success(request, f'Congrats! You have created a new recipe!')
            return redirect('/')
    else:
        c_recipe = RecipeCreateForm()
        c_ingredients = IngredientsCreateForm()
        c_steps = StepCreateForm()

    context = {
        'c_recipe': c_recipe,
        'c_ingredients': c_ingredients,
        'c-steps': c_steps
    }

    

    return render(request, 'recipe/recipe_form.html', context)

# class RecipeCreateView(LoginRequiredMixin, CreateView):
#     model = Recipe
#     fields = ['title']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class IngredientsCreateView(LoginRequiredMixin, CreateView):
#     model = Ingredients
#     fields = ['ingredients']

#     def form_valid(self, form):
#         print("Self **********",self.request, '**********', form)
#         form.instance.recipe = self.request.recipe_id
#         return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False
    
