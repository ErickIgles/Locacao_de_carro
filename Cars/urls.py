from django.urls import path
from .views import (
    indexView, 
    detailCar, 
    formRentCar, 
    rentCarUser, 
    carReturn, 
    makerList,
    search_cars,
    error404,
    error500
)

urlpatterns = [
    path('', indexView, name='index'),
    path('cars/detailCars/<int:pk>', detailCar, name='detail_car'),
    path('cars/rentalCars/<int:pk>', formRentCar, name='form_rent_car'),
    path('cars/rentCarUser/', rentCarUser, name='rent_car_user'),
    path('cars/carReturn/<int:pk>', carReturn, name='car_return'),
    path('cars/makerListCar/<int:pk>', makerList, name='maker_list'),
    path('cars/searchCar/', search_cars, name='search_cars'),
    path('erro404/', error404, name='error404'),
    path('erro500/', error500, name='error500'),
]
