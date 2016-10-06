from django import forms
from django.core.exceptions import ValidationError

from blog.models import Post


class PostForm(forms.ModelForm):

    # confirm_title = forms.CharField(
    #     label="confirm_title",
    #     required=True,
    # )

    class Meta:
        model = Post
        fields = '__all__' 

    def __init__(self, *args, **kwargs):

        # if kwargs.get('instance'):
        #     title = kwargs['instance'].title
        #     kwargs.setdefault('initial', {})['confirm_title'] = title

        return super(PostForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
           raise ValidationError("Title cannot be blank")

        if len(title) <5:
           raise ValidationError("Title is too short.")

        if len(title) >100:
           raise ValidationError("Title is too long.")

        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
           raise ValidationError("Post-text cannot be blank")

        if len(text) <140:
           raise ValidationError("Post-text is too short.")
           
        if len(text) >10000:
           raise ValidationError("Post-text is too long.")
        return text