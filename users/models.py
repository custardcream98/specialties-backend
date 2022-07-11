from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    '''
    User 모델, AbstractUser 클래스 상속해 사용했습니다.
    '''

    wallet_address = models.TextField(primary_key=True)
    # 지갑 주소를 PK로 삼습니다.
