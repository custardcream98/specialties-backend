from django.db import models
import core.models as coreModels


class PostEmoji(coreModels.Emotions):

    """ 포스팅 이모지 기록 """

    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="emojies")

class PostText(coreModels.CreatedModel):

    """ 포스팅 내용 """

    text = models.TextField()
    post_id = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="post_texts")


class Post(coreModels.AbstractContents):
    
    """ 포스팅 """

    title = models.CharField(max_length=100)
    creator = models.ForeignKey("users.User", on_delete=models.SET(coreModels.get_left_user), related_name="posts", null=True)
    category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, related_name="posts", null=True)

    # is_anonymous = models.BooleanField(default=False)

    def getContent(self):
        return self.post_texts.objects.latest('created').text
    def putEmoji(self, emoji):
        emojiDB = self.emojies.objects.get(emoji=emoji)
        if not emojiDB:
            newEmoji = PostEmoji(
                emoji=emoji,
                post=self
            )
            newEmoji.save()
        else:
            emojiDB.emoji_count += 1
            emojiDB.save()

    def __str__(self):
        return f'{self.id} | {self.title}'
    