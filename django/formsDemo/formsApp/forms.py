from django import forms

class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'Male'), ('female', 'Female')]

    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
