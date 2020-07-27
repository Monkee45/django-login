from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

#  subclass the UserCreationForm to get it to use the CustomUser model instead
# of the standard User model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', )
