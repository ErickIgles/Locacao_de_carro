from django.shortcuts import render, redirect ,get_object_or_404
from .models import Car, RentedCars, MakerCar
from .forms import RentCarForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q



def error404(request, exception):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')



def indexView(request):

    context = {
        'cars': Car.objects.all(),
        'maker_cars': MakerCar.objects.all()
    }

    return render(request, 'index.html', context)


def makerList(request, pk):

    cars = Car.objects.filter(car_maker=pk)

    return render(request, 'cars_templates/maker_car.html', {'cars': cars})


def search_cars(request):

    query = request.GET.get('q')
    cars = Car.objects.all()

    if query:
        cars = cars.filter(
            Q(car_model__icontains=query)|Q(car_maker__car_maker__icontains=query)
        )

    context = {
        'cars': cars,
        'query': query
    }

    return render(request, 'cars_templates/search_cars.html', context)


def detailCar(request, pk):

    car = get_object_or_404(Car, id=pk)
    status_available = (car.car_status)


    context = {
        'car': car,
        'status_car': status_available
    }
    return render(request, 'cars_templates/detail_cars.html', context)


@login_required(login_url='login')
def formRentCar(request, pk):
    car = get_object_or_404(Car, id=pk)

    if request.method == 'POST':
        user = request.user
        form = RentCarForm(data=request.POST)
        if form.is_valid():
            rent_car = form.save(commit=False)
            rent_car.user = user
            rent_car.car = car
            rent_car.rent_date = form.cleaned_data.get('rent_date')
            rent_car.return_date = form.cleaned_data.get('return_date')
            rent_car.save()
            messages.success(request, f'Carro {car.car_model} alugado com sucesso.')
            return redirect('rent_car_user')
    else:
        form = RentCarForm()
    return render(request, 'cars_templates/form_rent_car.html', {'form': form}) 


@login_required(login_url='login')
def rentCarUser(request):

    rented_cars = RentedCars.objects.filter(user=request.user)

    if rented_cars: 
        for car in rented_cars:

            if car.rent_date > car.return_date:
                difference = car.rent_date.day - car.return_date.day
            elif car.return_date > car.rent_date:
                difference = car.return_date.day - car.rent_date.day
            else:
                difference = 1
            value_rent = car.car.car_daily_price * difference
            context = {
                'rented_cars': rented_cars,
                'value_rent': value_rent
            }

    else:
        context = {}
    return render(request, 'cars_templates/rent_car.html', context)


@login_required(login_url='login')
def carReturn(request, pk):

    rented_car = get_object_or_404(RentedCars, user=request.user, car=pk)

    if request.method == 'POST':
        rented_car.car_return()
        rented_car.delete()

        messages.success(request, 'Aluguel cancelado com sucesso.')
        return redirect('rent_car_user')
    
    context = {
        'rented_car': rented_car
    }
    return render(request, 'cars_templates/rent_car.html', context)

