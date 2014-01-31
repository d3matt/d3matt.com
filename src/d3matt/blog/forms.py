from django import forms
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from blog.models import BlogPost

BLOG_LAYOUT=Layout(
        'title',
        'content',
    )
BLOG_SAVE = FormActions( Submit('save_changes', 'Save changes', css_class="btn-primary") )
BLOG_DRAFT_SAVE = FormActions(
    Submit('save_changes', 'Save changes', css_class="btn-primary"),
    Submit('save_draft', 'Save As Draft', css_class="btn-primary"))


class BlogForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = BlogPost
        fields = [ 'title', 'content' ]

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

class AddBlogForm(BlogForm):
    helper = FormHelper()
    helper.layout = Layout(BLOG_LAYOUT, BLOG_DRAFT_SAVE)

class EditBlogForm(BlogForm):
    helper = FormHelper()
    helper.layout = Layout(BLOG_LAYOUT, BLOG_SAVE)

class EditDraftBlogForm(BlogForm):
    helper = FormHelper()
    helper.layout = Layout(BLOG_LAYOUT, BLOG_DRAFT_SAVE)

class BlogAuthForm(AuthenticationForm):
    helper = FormHelper()
    helper.layout = Layout(
        'username',
        'password',
        FormActions( Submit('login', 'Login', css_class="btn-primary") )

    )
