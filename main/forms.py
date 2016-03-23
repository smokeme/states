from main.models import StateCities
from django import forms
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class CitySearchForm(forms.Form):
	city = forms.CharField(required=True, initial='Orem',validators=[alphanumeric])
	state = forms.CharField(required=True, initial='Utah',validators=[alphanumeric])

class CreateCityForm(forms.ModelForm):
	class Meta:
		model = StateCities
		fields = '__all__'

class CityEditForm(forms.ModelForm):
	class Meta:
		model = StateCities
		fields = '__all__'