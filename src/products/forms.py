from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title 	= forms.CharField(
			label = '',
			widget=forms.TextInput(
				attrs={
					"placeholder": "Enter title"
				}
			)
		)

	description = forms.CharField(
					label = '',
					widget = forms.Textarea(
						attrs = {
							"placeholder": "Enter description",
							"rows": 4
						}
					)
		)

	price 	= forms.DecimalField(
			label = '',
			widget = forms.NumberInput(
					attrs = {
						"placeholder" : "Enter price"
					}
				)
		)

	class Meta:
		model = Product 
		fields = [
			'title',
			'description',
			'price'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not len(title) > 3:
			raise forms.ValidationError("This is not a valid title")
		else: 
			return title

