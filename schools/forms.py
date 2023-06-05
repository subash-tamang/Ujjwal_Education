from django import forms

class ContactForm(forms.Form):
    user_name = forms.CharField(max_length=100)