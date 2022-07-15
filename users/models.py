from django.db import models
from django.contrib.auth.models import AbstractUser
from core.modules.randomId import RandomIdGenerator
randomNonceGenerator = RandomIdGenerator()


class User(AbstractUser):

    '''
    User 모델
    '''
    nickname = models.CharField(max_length=20, null=False)
    nonce = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        self.nonce = randomNonceGenerator.randomId(size=15)
        return super().save(*args, **kwargs)
    