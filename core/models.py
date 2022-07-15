from django.db import models
from django.contrib.auth import get_user_model


def get_left_user():
    return get_user_model().objects.get_or_create(nickname='탈퇴한 회원', username='0x0000000000')[0]

# def get_deleted_community():
#     return communityModels.objects.get_or_create()

class Emotions(models.Model):

    """ 감정표현 """

    emoji = models.CharField(max_length=5)
    emoji_count = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.emoji} {self.emoji_count}'

class CreatedAndUpdatedModel(models.Model):

    """ 생성 시간, 수정 시간 저장 """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CreatedModel(models.Model):

    """ 생성 시간만 저장 """

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class AbstractContents(CreatedAndUpdatedModel):
    
    """
    안건, 포스트, 댓글 등의 Abstract Model로,
    반드시 creator attribute와 getContent, putEmoji 함수를 override해줘야 합니다.
    """

    creator = models.TextField()

    def getCreatorName(self):
        return self.creator.nickname if self.creator is not None else "익명"
    def getContent(self):
        raise NotImplementedError( "getContent 정의해야 합니다." )
    def getEmojies(self):
        return list(map(lambda x: (x.emoji, x.emoji_count), self.emojies.objects.all()))
    def putEmoji(self, emoji):
        raise NotImplementedError( "putEmoji 정의해야 합니다." )
    def delEmoji(self, emoji):
        emojiDB = self.emojies.objects.get(emoji=emoji)
        emojiDB.emoji_count -= 1
        if emojiDB.emoji_count == 0:
            emojiDB.delete()
        else:
            emojiDB.save()

    class Meta:
        abstract = True