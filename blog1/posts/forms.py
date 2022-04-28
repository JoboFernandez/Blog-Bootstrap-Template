from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'name': "usercomment",
                'id': "usercomment",
                'placeholder': "Type your comment",
                'class': "form-control",
                'rows': "5",
            }
        ),
        label=''
    )

    class Meta:
        model = Comment
        exclude = ['user', 'post']