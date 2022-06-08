from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)


# class UserLoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")

#         # user_qs = User.objects.filter(username=username)
#         # if user_qs.count() == 1:
#         #     user = user_qs.first()
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError("This user does not exist")
#             if not user.check_password(password):
#                 raise forms.ValidationError("Incorrect passsword")
#             if not user.is_active:
#                 raise forms.ValidationError("This user is not longer active.")
#         return super(UserLoginForm, self).clean(*args, **kwargs)



class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'placeholder': 'Ingrese usuario',
            'class': 'form-control'
        }
        self.fields['password'].widget.attrs = {
            'placeholder': 'Ingrese contraseña',
            'class': 'form-control'
        }