import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.crypto.nonce import getNewNonce


class User(AbstractUser):

    '''
    User 모델
    '''

    nonce = models.BigIntegerField()
    wallet_address = models.CharField(primary_key=True, max_length=37)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __str__(self):
        return f'{"Addr " + self.wallet_address if self.wallet_address != "" else ""}'
    def save(self, *args, **kwargs):
        self.nonce = getNewNonce()
        return super().save(*args, **kwargs)