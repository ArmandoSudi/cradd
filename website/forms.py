from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Votre Nom',max_length=200)
    email = forms.EmailField(label='Votre Email')
    subject = forms.CharField(label='Sujet', max_length=100)
    message = forms.CharField(widget=forms.Textarea)