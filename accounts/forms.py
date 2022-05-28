from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser


class CustomCreatUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', )


class CustomChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
