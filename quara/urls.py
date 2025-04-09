from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewset, AnswerViewset, LikeViewSet, signup_view, login_view

router = DefaultRouter()
router.register(prefix=r'questions', viewset=QuestionViewset, basename='question')
router.register(prefix=r'answers', viewset=AnswerViewset, basename='answer')
router.register(prefix=r'likes', viewset=LikeViewSet, basename='like')

urlpatterns = [
    path('', include(router.urls)),
    # path('signup/', signup_view, name='signup'),
    # path('login/', login_view, name='login'),
]
