from django import forms

from django_countries.fields import CountryField

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control'
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-control'
    }))
    Email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'example@email.com',
        'class': 'form-control'
    }))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder': '090123456789',
        'class': 'form-control'
    }))

    country = CountryField(blank_label= ('country')).formfield(attrs={
        'class': 'form-label mt-4'
    })


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your full name'
    }))
    your_email = forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'example@gmail.com'
    }))
    message_body = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'How do you want to get involved?',
        'rows':4
    }))
