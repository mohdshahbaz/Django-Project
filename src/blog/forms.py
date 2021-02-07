from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
  title 	= forms.CharField(
        label = '',
        widget=forms.TextInput(
          attrs={
            "placeholder": "Enter title"
          }
        )
      )

  content = forms.CharField(
          label = '',
          widget = forms.Textarea(
            attrs = {
              "placeholder": "Enter content",
              "rows": 4
            }
          )
    )

  # active 	= forms.BooleanField(
  #     widget = forms.CheckboxInput(
  #       )
  #   )

  class Meta:
    model = Article
    fields = {
      'title', 
      'content', 
      'active'
    }