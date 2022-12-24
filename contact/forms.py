from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)
    