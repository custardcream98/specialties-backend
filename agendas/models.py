from datetime import timedelta
from django.db import models
import core.models as coreModels


class AgendaEmoji(coreModels.Emotions):

    """ 안건 이모지 기록 """

    agenda = models.ForeignKey("agendas.Agenda", on_delete=models.CASCADE, related_name="emojies")

class Agenda(coreModels.AbstractContents):

    """ 안건 모델 """
    
    community = models.ForeignKey("communities.Community", on_delete=models.CASCADE, related_name="agendas")
    creator = models.ForeignKey("users.User", on_delete=models.SET(coreModels.get_left_user), related_name="agndaCreated", null=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()
    deadline = models.DateTimeField()

    def getContent(self):
        return self.content
    def putEmoji(self, emoji):
        emojiDB = self.emojies.objects.get(emoji=emoji)
        if not emojiDB:
            newEmoji = AgendaEmoji(
                emoji=emoji,
                agenda=self
            )
            newEmoji.save()
        else:
            emojiDB.emoji_count += 1
            emojiDB.save()

    def save(self, *args, **kwargs):
        self.deadline = self.created + timedelta(days=7)
        return super().save(*args, **kwargs)