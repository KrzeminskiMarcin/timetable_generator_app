from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError
from bootstrap_modal_forms.forms import BSModalModelForm
def validate_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError("E-mail is already is taken.")

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        widgets ={'user': forms.HiddenInput()}

class LekcjaForm(forms.ModelForm):
    class Meta:
        model = Lekcja
        fields = '__all__'
        widgets ={'plan': forms.HiddenInput()}

    def clean(self):
            godzina1 = self.cleaned_data['godzinazakonczeniaa']
            godzina2 = self.cleaned_data['godzinarozpoczecia']
            if godzina1 <= godzina2:
                raise ValidationError("Incorrect class time frames.")


