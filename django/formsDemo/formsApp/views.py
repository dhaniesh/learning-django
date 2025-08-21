from django.shortcuts import render
from . import forms
# Create your views here.
def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            print('firstName', form.cleaned_data['firstName'])
    return render(request, 'UserRegistration.html', {'form': form}) 