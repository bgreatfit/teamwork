from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, help_text="enter username")
    email = models.EmailField(_('email address'), unique=True)
    #
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.email
