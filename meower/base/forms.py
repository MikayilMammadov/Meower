from django import forms
from .models import Tweet, Comment, User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['topic', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please retype the password.")

        return cleaned_data