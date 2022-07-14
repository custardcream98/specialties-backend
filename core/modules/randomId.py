import random
import string
from datetime import datetime


class RandomIdGenerator():

    """
    랜덤으로 ID를 생성해줍니다.  

    객체 생성시에 choices를 정할 수 있고,  

    `rendomId(seed, size)` 메소드를 사용하면 됩니다. 시드를 지정하지 않을 경우 현재 시각의 timestamp가 시드값이 됩니다.
    """

    def __init__(self, choices =  string.ascii_letters + string.digits):
        self.choices = choices
    def randomId(self, seed = int(datetime.now().timestamp()), size=8):
        return ''.join(random.SystemRandom(seed).choice(self.choices) for _ in range(size))
