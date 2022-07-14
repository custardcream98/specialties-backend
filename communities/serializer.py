from rest_framework import serializers
from categories.serializer import CategorySerialzer
from communities import models as communityModels


class CommunitySerialzer(serializers.ModelSerializer):
    total_member = serializers.SerializerMethodField()
    
    def get_total_member(self, community):
        return community.totalMember() 

    class Meta:
        model = communityModels.Community
        exclude = ['total_member', 'categories']

class CommunityDetailSerialzer(serializers.ModelSerializer):
    total_member = serializers.SerializerMethodField()
    core_members = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()

    categories = serializers.SerializerMethodField()
    
    def get_total_member(self, community):
        return community.totalMember()

    def get_core_members(self, community):
        result = []
        for m in community.core_members.objects.all():
            result.append(m.username)
        return result
    
    def get_members(self, community):
        result = []
        for m in community.members.objects.all():
            result.append(m.username)
        return result

    def get_categories(self, community):
        result = []
        for c in community.categories.objects.all():
            result.append(CategorySerialzer(c))
        return result

    class Meta:
        model = communityModels.Community
        fields = '__all__'