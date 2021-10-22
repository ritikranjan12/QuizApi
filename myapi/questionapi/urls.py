from django.urls import path
from .views import QuestionAPIView,QuestionDetail
urlpatterns = [
    path('',QuestionAPIView.as_view()),
    path('<int:pk>/',QuestionDetail.as_view())
]