from django.db import models

from user.models import CustomUser


class UserPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=30)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} | {self.title}'


class UserAnswer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='answers')
    description = models.TextField()
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_post} | {self.created_at}'
