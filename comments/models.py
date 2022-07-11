from django.db import models
import core.models as coreModels


class CommentEmoji(coreModels.Emotions):

    """ 댓글 이모지 기록 """

    comment = models.ForeignKey("comments.Comment", on_delete=models.CASCADE, related_name="emojies")

class Comment(coreModels.AbstractContents):

    """ 댓글 """

    creator = models.ForeignKey("users.User", on_delete=models.SET(coreModels.get_left_user), related_name="comments", null=True)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    is_deleted = models.BooleanField(default=False)

    def getContent(self):
        return self.comment if not self.is_deleted else "삭제된 댓글"
    def putEmoji(self, emoji):
        emojiDB = self.emojies.objects.get(emoji=emoji)
        if not emojiDB:
            newEmoji = CommentEmoji(
                emoji=emoji,
                comment=self
            )
            newEmoji.save()
        else:
            emojiDB.emoji_count += 1
            emojiDB.save()

    def __str__(self):
        return f'{self.id} | {self.getComment()}'
    