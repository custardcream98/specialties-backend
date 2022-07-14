from django.db import models
from django.contrib.auth.models import AbstractUser
from core.modules.randomId import RandomIdGenerator
randomNonceGenerator = RandomIdGenerator()


class User(AbstractUser):

    '''
    User 모델
    '''

    nonce = models.CharField(max_length=15)
    wallet_address = models.CharField(primary_key=True, max_length=37)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __str__(self):
        return f'{"Addr " + self.wallet_address if self.wallet_address != "" else ""}'
    def save(self, *args, **kwargs):
        self.nonce = randomNonceGenerator.randomId(size=15)
        return super().save(*args, **kwargs)