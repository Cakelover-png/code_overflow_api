from rest_framework import serializers

from post_answer_api.models import UserPost, UserAnswer


class UserAnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserAnswer
        fields = "__all__"


class UserPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    answers = UserAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = UserPost
        fields = "__all__"
