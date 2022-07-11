from django.db import models
import core.models as coreModels


class Community(coreModels.CreatedAndUpdatedModel):
    
    """ 커뮤니티 모델 """

    name = models.CharField(max_length=80)
    leader = models.ForeignKey("users.User", related_name="communities_leader", on_delete=models.SET(coreModels.get_left_user), null=True)

    core_members = models.ManyToManyField("users.User", blank=True, related_name="communities_core")
    members = models.ManyToManyField("users.User", related_name="communities_member", blank=True)

    def __str__(self):
        return f'Community {self.name} | Leader {self.leader}'