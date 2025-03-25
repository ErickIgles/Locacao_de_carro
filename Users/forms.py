from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm



from .models import CustomUser

        

class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'cpf')
        labels = {'username': 'Username/E-mail'}


    def save(self, commit=True):
        user = super().save(commit=False) # recupera os dados do usuário antes de salvar.
        user.set_password(self.cleaned_data['password1']) # criptografa a senha.
        user.username = self.cleaned_data['email'] # torna o username igual o usuário (email)
        if commit:
            user.save()
        return user



# não utilizar na atualização de usuários normais, fora da admin.
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'cpf')



class NewUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'cpf')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class LoginUserForm(AuthenticationForm):

    model = CustomUser
    fields = ('email', 'password1')
    

