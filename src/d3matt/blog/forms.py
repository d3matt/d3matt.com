from django import forms
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from blog.models import BlogPost

class AddBlogForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    helper = FormHelper()

    helper.layout = Layout(
        'title',
        'content',
        FormActions( Submit('save_changes', 'Save changes', css_class="btn-primary") )
    )

    def clean_title(self):
        txt = self.cleaned_data['title']
        if len(txt) < 4:
            raise forms.ValidationError("title must be longer than 4 characters...")
        return txt

    def clean_content(self):
        txt = self.cleaned_data['content']
        if len(txt.split()) < 2:
            raise forms.ValidationError("blog post must consist of more than 2 words!")
        return txt

class BlogAuthForm(AuthenticationForm):
    helper = FormHelper()
    helper.layout = Layout(
        'username',
        'password',
        FormActions( Submit('login', 'Login', css_class="btn-primary") )

    )
