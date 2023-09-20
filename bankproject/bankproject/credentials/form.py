# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    dob = forms.DateField(null=True, blank=True)
    age = forms.IntegerField(null=True, blank=True)
    gender = forms.CharField(max_length=10, null=True, blank=True)
    phno = forms.CharField(max_length=15, null=True, blank=True)
    mailid = forms.EmailField(null=True, blank=True)
    address = forms.TextInput(null=True, blank=True)
    district = forms.CharField(max_length=50, null=True, blank=True)
    account_type = forms.CharField(max_length=50, null=True, blank=True)
    materials_provided = forms.ManyToManyField('Material', blank=True)

    class Meta:
        model = UserCreationForm
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
