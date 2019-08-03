from django import forms

class RegistrationForm(forms.Form):
    your_name = forms.CharField(label='Enter Your Name',max_length=100)
    father_name = forms.CharField(label='Enter Father Name',max_length=100)
    your_email = forms.EmailField(label='Enter Your E-mail')