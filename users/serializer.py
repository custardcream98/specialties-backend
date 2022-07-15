from rest_framework import serializers
from users import models as userModels


class UserSerialzer(serializers.ModelSerializer):
    wallet_address = serializers.SerializerMethodField('get_username')

    def get_username(self, user):
        return user.username

    class Meta:
        model = userModels.User
        fields = ['nickname', 'avatar', 'wallet_address']