from django import forms
from catalog.models import Product, Version

#прикручиваю формсет#
#from django.forms.models import inlineformset_factory

#VersionFormset = inlineformset_factory(Product, Version, extra=1)
#прикручиваю формсет#


class ProductForm(forms.ModelForm):

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            #field.help_text = 'Some help text for field'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for item in self.forbidden_words:
            if item in cleaned_data:
                raise forms.ValidationError(f'Запрещенное слово "{item}" в наименовании продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for item in self.forbidden_words:
            if item in cleaned_data:
                raise forms.ValidationError('Запрещенное слово в описании продукта')
        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        #fields = ('is_active', )
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
           # field.help_text = 'Some help text for field'
            #field.help_text = 'Например,'
