from rest_framework import serializers
from users import models as userModels


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = userModels.User
        fields = ['username', 'avatar', 'wallet_address']