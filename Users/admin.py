from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUserCreateForm # formulário de criação de usuário
    form = CustomUserChangeForm # formulário de edição de usuário
    model = CustomUser # modelo que será usado para registro.

    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'is_staff')
    list_display_links = ('first_name', 'last_name', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields':('first_name', 'last_name', 'phone_number', 'cpf')}),
        ('Permissões', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields':('last_login', 'date_joined')}),
    )