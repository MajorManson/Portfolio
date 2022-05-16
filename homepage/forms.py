from django import forms

class ContactMeForm(forms.Form):
    name = forms.CharField(label='sr-only',
                           widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                         'class': 'form-control',
                                                         'id':'c_name'}),
                           required=True)

    email = forms.EmailField(label='sr-only',
                             widget=forms.TextInput(attrs={'placeholder': 'E-mail',
                                                           'class': 'form-control',
                                                           'id':'c_email'}),
                             required=True)

    message = forms.CharField(label='sr-only',
                              widget=forms.TextInput(attrs={'placeholder': 'Message',
                                                            'class': 'form-control',
                                                            'id':'c_message'}),
                              required=True)