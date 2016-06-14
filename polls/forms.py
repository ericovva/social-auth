from __future__ import unicode_literals
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from polls.models import MyUser,Game,Comment
from django import forms
from django.conf import settings

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('email',)
        
        # def clean_username(self):
        #     username = self.cleaned_data["username"]
        #     try:
        #         MyUser.objects.get(username=username)
        #     except MyUser.DoesNotExist:
        #         return username
        #     raise forms.ValidationError(self.error_messages['duplicate_username'])
        # def clean_email(self):
        #     email = self.cleaned_data["email"]
        #     try:
        #         MyUser.objects.get(email=email)
        #     except MyUser.DoesNotExist:
        #         return email
        #     raise forms.ValidationError(self.error_messages['duplicate_email'])

class CommentsForm(forms.ModelForm):
    #text = forms.CharField(
     #widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))
    class Meta:
        fields = ('text',)#,'game','user')
        model = Comment
        def clean_text(self):
            text = self.cleaned_data["text"]
            if text == "":
                raise forms.ValidationError("Type anything in your comment")
            return text
        #def save(self):
         #   print(self)
            # print("SS")
            # data = self.cleaned_data
            # e = Comment(text = data["text"])
            # e.save()
            # print(e.id)
            # data = self.cleaned_data
            # g = Game.objects.get(game_id)
            # u = MyUser.objects.get(user_id)
            # e = Comment(text = data["text"])
            # g.comment_set.add(e)
            # u.comment_set.add(e)
            # e.save()
# class LikeForm(forms.ModelForm):
#     class Meta:
#         fields = ("",)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50,required=False)
    file = forms.FileField()
