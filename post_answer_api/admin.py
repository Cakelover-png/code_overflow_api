from django.contrib import admin

from post_answer_api.models import UserPost, UserAnswer

admin.site.register([UserPost, UserAnswer])
