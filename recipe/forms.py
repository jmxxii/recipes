from django import forms
from .models import Recipe, Ingredients, Step


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title']

class IngredientsCreateForm(forms.ModelForm):
    
    class Meta:
        model = Ingredients
        fields = ['ingredients']

class StepCreateForm(forms.ModelForm):

    steps = forms.Textarea()

    class Meta:
        model = Step
        fields = ['steps']