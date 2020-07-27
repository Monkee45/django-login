from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from users.managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email_address'), unique=True)
    # define the unique identifier for the User model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # specifies that all objects for the class come from CustomUserManager
    objects = CustomUserManager()

    def __str__(self):
        return self.email
