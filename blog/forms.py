from django import forms

class CommentForm(forms.Form):
    # this is the max length of the character field, it has 60 characters
    # You’ll also notice an argument widget has been passed to both the fields
    # The author field has the forms.TextInput widget. This tells Django to load 
    # this field as an HTML text input element in the templates. The body field 
    # uses a forms.TextArea widget instead, so that the field is rendered as an HTML text area element.

    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
                # this is a form and it is indexed as such in the class
                # it has a word in it already 
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )