from django import forms
from captcha.fields import CaptchaField
from .models import Comments


class CommentModelForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comments
        fields = ['nickname', 'comment']
