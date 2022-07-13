import datetime as dt
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import rest_framework.status as status
import users.models as userModels
import communities.models as communityModels


class CommunityView(APIView):
    '''
    커뮤니티 관련 뷰입니다.

    한가지 URL을 가지고도 GET, POST 등에 따라 달리 작동하는,
    RESTful하도록 설계하는것이 목표입니다.
    '''

    permission_classes = [IsAuthenticated]

    '''
    POST 커뮤니티 생성
    '''
    def post(self, request):
        data = request.data
        leader_instance = request.user
        timestamp = int(dt.datetime.now().timestamp())

        community_instance = communityModels.Community.objects.create(
            id = f'{leader_instance.wallet_address}{timestamp}',
            name = data['name'],
            description = data['description'],
            related_asset = data['related_asset'],

            leader = leader_instance,
        )

        return Response({"created_community_id":community_instance.id}, status=status.HTTP_200_OK)
    
    '''
    유저가 가입해있는 커뮤니티 정보 리턴
    '''
    # def get(self, request):

