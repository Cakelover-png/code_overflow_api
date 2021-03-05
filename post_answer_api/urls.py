from django.urls import path, include

from post_answer_api.views import UserPostView, UserPostDetailView, UserAnswerView, UserAnswerDetailView

urlpatterns = [
    path('user-posts/', UserPostView.as_view(), name='user-posts-api'),
    path('user-posts/<int:pk>', UserPostDetailView.as_view(), name='user-post-detail-api'),
    path('answers/', UserAnswerView.as_view(), name='answers-api'),
    path('answers/<int:pk>', UserAnswerDetailView.as_view(), name='answers-detail-api'),
]
