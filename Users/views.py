from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreateForm, NewUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm



def index(request):
    return render(request, 'index.html')


def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, f'Usuário(a) {user.first_name} cadastro com sucesso.')
            return redirect('index')
    
    else:
        form = CustomUserCreateForm()
    return render(request, 'users_templates/create_user.html', {'form': form})



def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'users_templates/login.html', {'form': form})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('index')

    

@login_required(login_url='login')
def profile_user(request):
    return render(request, 'users_templates/profile_user.html')


@login_required(login_url='login')
def update_data(request):
    user = request.user

    if request.method == 'POST':
        form = NewUserChangeForm(request.POST, instance=user) # passar novos dados e associar ao usuário

        if form.is_valid():
            user = form.save()

            messages.success(request, f'Dados de {user.get_full_name()} atualizados com sucesso.')
            return redirect('profile_user')
    else:
        form = NewUserChangeForm(user)
    return render(request, 'users_templates/profile_user.html', {f'form': form})


@login_required(login_url='login')
def update_password(request):
    user = request.user
    
    if request.method == 'POST':

        if user.is_authenticated:
            form = SetPasswordForm(user, request.POST) 
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Senha alterada com sucesso.')
                return redirect('profile_user')
    
    else:
        form = SetPasswordForm(user)
    return render(request, 'users_templates/update_password.html', {'form': form})


@login_required(login_url='login')
def delete_account(request):

    if request.method == 'POST':
        user = request.user
        user = get_object_or_404(CustomUser, id=user.id)
        user.delete()
        logout_user(request)
        messages.success(request, f'Conta deletada com sucesso.')
        return redirect('index')

    return render(request, 'users_templates/delete_account.html')


def about(request):
    return render(request, 'about.html')


# Deve-se passar o user mais a requisição quando preciso associar alterações ao usuário. Exemplo: SetPasswordForm(user, request.POST) / NewUserChangeForm(request.POST, instance=user).