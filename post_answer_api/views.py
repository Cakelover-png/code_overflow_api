from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from post_answer_api.models import UserPost, UserAnswer
from post_answer_api.permissions import IsOwnerOrReadOnly
from post_answer_api.serializers import UserPostSerializer, UserAnswerSerializer


class UserPostView(ListCreateAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('title',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserPostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class UserAnswerView(ListCreateAPIView):
    serializer_class = UserAnswerSerializer
    queryset = UserAnswer.objects.all()
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.queryset.filter(user=request.user, user_post=request.data['user_post']).exists():
            return Response({'Details': 'You already answered to this post'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAnswerDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserAnswerSerializer
    queryset = UserAnswer.objects.all()
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
