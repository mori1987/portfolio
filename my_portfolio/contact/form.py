from django import forms
from . models import Contact
# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=50)
#     phone_number= forms.NumberInput()
#     email= forms.EmailInput()
#     message= forms.TextInput()


class Contact_Form(forms.ModelForm):
    class Meta:
        model= Contact
        fields= ('name','phone_number','email','message')
