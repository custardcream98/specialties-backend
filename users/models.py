from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    '''
    User 모델
    '''

    avatar = models.ImageField(upload_to='avatars', blank=True)
    wallet_address = models.TextField(default="")

    def __str__(self):
        return f'ID {self.id} {self.username}{" | Addr " + self.wallet_address if self.wallet_address != "" else ""}'