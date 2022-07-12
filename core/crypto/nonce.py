import random


def getNewNonce() -> int:
    return random.randrange(10000000000,99999999999)