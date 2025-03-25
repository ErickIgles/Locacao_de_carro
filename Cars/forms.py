from django import forms
from django.core.validators import RegexValidator
from .models import RentedCars, Car


class CarAdminForm(forms.ModelForm):
    car_plate = forms.CharField(label='Placa',max_length=7, validators=[RegexValidator(r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$', 'Placa inválida! O formato correto é AAA9A99 (exemplo: ABC1D23).')])

    class Meta:
        model = Car
        fields = '__all__'


class RentCarForm(forms.ModelForm):

    class Meta:
        model = RentedCars
        fields = ('rent_date', 'return_date',)

