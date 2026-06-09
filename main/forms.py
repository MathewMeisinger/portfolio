# imports
from django import forms


class ContactForm(forms.Form):
    # Basic sender details used to identify who submitted the message.
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Name",
            "class": "contact-input"
        })
    )

    # EmailField ensures the submitted value is a valid email address.
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Your Email Address",
            "class": "contact-input"
        })
    )

    # Short subject line for the outgoing email.
    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Subject",
            "class": "contact-input"
        })
    )

    # Main body of the user's message, shown in a multi-line textarea.
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Your Message",
            "class": "contact-input",
            "rows": 6
        })
    )
