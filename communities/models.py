from unicodedata import category
from django.db import models
import core.models as coreModels


class Community(coreModels.CreatedAndUpdatedModel):
    
    """ 커뮤니티 모델 """

    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=80)
    description = models.TextField(null=True) # 커뮤니티 설명, 소개
    banner = models.ImageField(upload_to='avatars', blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    related_asset = models.CharField(max_length=100, null=True) # 관련있는 NFT 혹은 자산의 이름
    # 이 부분은 한글 <-> 컨트랙트 주소 검색 데이터가 마땅치 않으므로
    # 직접 구축하는것이 좋아 보입니다.
    related_asset_contract = models.CharField(max_length=40, null=True) # 관련있는 NFT 혹은 코인의 주소
    leader = models.ForeignKey("users.User", related_name="communities_leader", on_delete=models.SET(coreModels.get_left_user), null=True)

    core_members = models.ManyToManyField("users.User", blank=True, related_name="communities_core")
    members = models.ManyToManyField("users.User", related_name="communities_member", blank=True)

    # _total_member = 0
    # @property
    # def total_member(self):
    #     return self._total_member

    # _categories = []
    # @property
    # def categories(self):
    #     for c in self.categories.objects.all():
    #         self._categories.append()

    def __str__(self):
        return f'Community {self.name} | Leader {self.leader}'

    def totalMember(self):
        return self.core_members.objects.count() + self.members.objects.count() + 1
    def categoryList(self):
        category = []
        for c in self.categories.objects.all():
            category.append(c)
        return category