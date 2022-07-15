from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status
import categories.models as categoryModels
import communities.models as communityModels
from communities.serializer import CommunitySerialzer, CommunityDetailSerialzer
from core.modules.randomId import RandomIdGenerator
randomIdGenerator = RandomIdGenerator()


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

        community_instance = communityModels.Community.objects.create(
            id = randomIdGenerator.randomId(seed=leader_instance.username, size=10),
            name = data['name'],
            description = data['description'],
            related_asset = data['related_asset'],

            leader = leader_instance,
        )

        categoryModels.Category.objects.create(
            id = randomIdGenerator.randomId(size=10),
            name = "자유게시판",
            order = 0,
            open_to=categoryModels.Category.OPEN_TO_ALL,
            community=community_instance
        )

        return Response(CommunitySerialzer(community_instance).data, status=status.HTTP_200_OK)
    
    '''
    유저가 가입해있는 커뮤니티 정보 리턴
    '''
    def get(self, request):
        user = request.user

        response = {
            "leader_of" : [],
            "core_of" : [],
            "member_of" : [],
        }

        for c in user.communities_leader.objects.all():
            response["leader_of"].append(CommunitySerialzer(c).data)
        for c in user.communities_core.objects.all():
            response["core_of"].append(CommunitySerialzer(c).data)
        for c in user.communities_member.objects.all():
            response["member_of"].append(CommunitySerialzer(c).data)

        return Response(response, status=status.HTTP_200_OK)

class CertainCommunityView(APIView):
    """
    특정 커뮤니티의 세부정보를 확인하는 뷰입니다.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, community_id):
        community_instance = communityModels.Community.objects.get(id = community_id)

        return Response(CommunityDetailSerialzer(community_instance).data, status=status.HTTP_200_OK)

