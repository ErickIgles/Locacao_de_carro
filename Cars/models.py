from django.core.validators import RegexValidator
from django.utils.timezone import now
from datetime import timezone, timedelta
from django.db import models
from stdimage.models import StdImageField
import uuid

from Users.models import CustomUser



def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    
    created = models.DateField('Criação', auto_now_add=True)
    modified = models.DateField('Atualizado', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class MakerCar(Base):

    car_maker = models.CharField('Fabricante', max_length=200)


    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
    

    def __str__(self):
        return self.car_maker


class Car(Base):
    """
        car_maker - Fabricante
        car_model - Modelo
        car_year - Ano de Fabricação
        car_mileage - Kilometragem
        car_daily_price - Valor da diária
        car_rent - Locadora
        car_color - Cor do carro
    """

    car_maker = models.ForeignKey(MakerCar, on_delete=models.PROTECT, verbose_name='Fabricante')
    car_model = models.CharField('Modelo', max_length=140)
    car_year = models.IntegerField('Ano')
    car_plate = models.CharField('Número da Placa', max_length=7, unique=True, validators=[RegexValidator(r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$', 'Placa inválida! O formato correto é AAA9A99 (exemplo: ABC1D23).')])
    car_plate = models.CharField('Número da Placa', max_length=7, unique=True)
    car_daily_price = models.DecimalField('Valor diário', max_digits=8, decimal_places=2)
    car_color = models.CharField('Cor', max_length=140)
    car_image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':420, 'height':480, 'crop':True}}, blank=True)
    car_status = models.BooleanField('Status', default=True)


    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    
    def __str__(self):
        return f'{self.car_model} {self.car_maker}'



class RegisterRentCarUser(Base):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Usuário')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Carro Alugado')
    rent_date = models.DateTimeField(auto_now_add=True, verbose_name='Data do aluguel')
    return_date = models.DateTimeField(null=True, blank=True, verbose_name='Data de devolução')

    class Meta:
        verbose_name = 'Registro de Locação'
        verbose_name_plural = 'Registro de Locações'


    def __str__(self):
        return f'Registro de locação realizado com sucesso.'
    

class RentedCars(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Usuário')
    car = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name='Carro Alugado')
    rent_date = models.DateField(verbose_name='Data do aluguel')
    return_date = models.DateField(null=True, blank=True, verbose_name='Data de devolução')


    class Meta:
        verbose_name = 'Tabela de carro alugado'
        verbose_name_plural = 'Tabelas de carros alugados'
    

    def __str__(self):
        return f'Carro {self.car.car_model} alugado com sucesso.'
    

    def save(self, commit=True):


        if self.car.car_status is False:
            pass

        else:
            register = RegisterRentCarUser(
                user=self.user,
                car=self.car,
                rent_date=self.rent_date,
                return_date=self.return_date
            )

            register.save()

            self.car.car_status = False
            self.car.save()

        return super().save()
    

    def car_return(self):

        if self.car.car_status is False:
            self.car.car_status = True
            self.car.save()


