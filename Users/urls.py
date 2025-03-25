from django.urls import path
from .views import (
    index, 
    create_user, 
    login_user, 
    logout_user, 
    profile_user, 
    update_data,
    update_password,
    delete_account,
    about,
    )

urlpatterns = [
    path('', index, name='index'),
    path('create_user/', create_user, name='create_user'),
    path('login/', login_user, name='login'),
    path('logout_user/', logout_user, name='logout_user'),
    path('perfil_user/', profile_user, name='profile_user'),
    path('update_data/', update_data, name='update_data'),
    path('update_password/', update_password, name='update_password'),
    path('delete_account/>', delete_account, name='delete_account'),
    path('about/', about, name='about'),
]