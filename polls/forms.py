from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from polls.models import MyUser,Game,Comment
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('email','username')
        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                MyUser.objects.get(username=username)
            except MyUser.DoesNotExist:
                return username
            raise forms.ValidationError(self.error_messages['duplicate_username'])

class CommentsForm(forms.ModelForm):
    #text = forms.CharField(
     #widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))
    class Meta:
        fields = ('text','game','user')
        model = Comment
