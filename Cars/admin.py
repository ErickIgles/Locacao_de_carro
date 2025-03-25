from django.contrib import admin
from .forms import CarAdminForm
from .models import (
    Car, 
    MakerCar, 
    RentedCars, 
    RegisterRentCarUser,
)


# Tabela de carros
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm
    list_display = ('car_maker', 'car_model', 'car_year', 'car_plate', 'car_color', 'car_status',
                    'created', 'modified')
    
    list_display_links = ('car_maker', 'car_model',)


# Tabela de Marcas dos carros
@admin.register(MakerCar)
class MakeCarAdmin(admin.ModelAdmin):
    list_display = ('car_maker',)
    list_display_links = ('car_maker',)


@admin.register(RentedCars)
class RentedCars(admin.ModelAdmin):
    list_display = ('user', 'car', 'rent_date', 'return_date',)
    list_display_links = ('user', 'car',)


@admin.register(RegisterRentCarUser)
class RegisterRentCarUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'rent_date', 'return_date',)
    list_display_links = ('user', 'car',)
