from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from . import validators

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() 
    
    class Meta:
        model = User
        fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
# class RegistrationFormUniqueEmail(UserRegisterForm):
#     """
#     Subclass of ``RegistrationForm`` which enforces uniqueness of
#     email addresses.
#     """
#     def __init__(self, *args, **kwargs):
#         super(RegistrationFormUniqueEmail, self).__init__(*args, **kwargs)
#         email_field = User.get_email_field_name()
#         self.fields[email_field].validators.append(
#             validators.CaseInsensitiveUnique(
#                 User, email_field,
#                 validators.DUPLICATE_EMAIL
#             )
#         )