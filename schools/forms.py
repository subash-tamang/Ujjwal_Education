from django import forms
from .models import Contact

# class ContactForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages= {
#         "required" : "Your name must not be empty!",
#         "max_length": "Please enter shorter name less than 100 characters!",
#     })
#     message = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=300)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {  # labels key for setting label  
            "name": "Your Name",  # "name" -> name of property of Contact model
            "message": "Your Message",
            "rating": "Your Rating",
        }
        error_messages = {
            "name": {
                "required": "Your name must not be empty!",  # required, max_length are error identifiers
                "max_length": "Please enter shorter name less than 100 characters!",
            },
            "rating": {
                "required": "Rating must not be empty!",
            }
        }
           
