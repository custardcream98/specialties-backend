from rest_framework import serializers
import categories.models as categoryModels


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = categoryModels.Category
        fields = ['id', 'name', 'open_to']