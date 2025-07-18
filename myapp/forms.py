from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    
    def message(self):
        print(f"Thank you for contacting us {self.cleaned_data['name']}.")