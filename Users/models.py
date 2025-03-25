from django.db import models


from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('E-mail requerido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff precisar ser is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser precisa ser is_superuser = True')
        
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    phone_number = models.CharField('Telefone', max_length=11, blank=True, null=True)
    cpf = models.CharField('cpf', max_length=11, unique=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf']
    
    def __str__(self):
        return self.email
    

    objects = UserManager()
