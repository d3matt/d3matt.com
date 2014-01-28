from django import forms
from blog.models import BlogPost

class AddBlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
        """sets pretty stuff for bootstrap"""
        super(AddBlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'Content of Post'

    def clean_title(self):
        txt = self.cleaned_data['title']
        if len(txt) < 4:
            raise forms.ValidationError("title must be longer than 4 characters...")
        return txt

    def clean_content(self):
        txt = self.cleaned_data['content']
        if len(txt.split()) < 2:
            raise forms.ValidationError("blog post must consiste of more than 2 words!")
        return txt

