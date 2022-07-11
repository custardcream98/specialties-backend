from unicodedata import category
from django.db import models
import users.models as userModels


class OpenTo(models.Model):
    
    """ 카테고리가 특정인 공개일 경우 OpenTo가 생깁니다. """

    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE, related_name="open_to_list")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="open_to_list")


class Category(models.Model):

    """ 커뮤니티 내의 카테고리 """

    OPEN_TO_ALL = 'all'
    OPEN_TO_NONE = 'non'
    OPEN_TO_CERTAIN = 'cer'

    OPEN_TO_CHOICES = (
        (OPEN_TO_ALL, "전체공개"),
        (OPEN_TO_NONE, "비공개"),
        (OPEN_TO_CERTAIN, "특정인 공개")
    )

    community = models.ForeignKey("communities.Community", on_delete=models.CASCADE, related_name="categories")

    open_to = models.CharField(choices=OPEN_TO_CHOICES, max_length=3, blank=False)

    def isAbleToGetIn(self, user:userModels.User):
        if (self.community.leader == user):
            return True
        elif (self.open_to == self.OPEN_TO_CERTAIN):
            for userAble in OpenTo.objects.filter(category = self.id):
                if (userAble.user == user):
                    return True
        elif (self.open_to == self.OPEN_TO_ALL):
            return True
        else:
            return False
