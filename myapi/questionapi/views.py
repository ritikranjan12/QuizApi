from django.shortcuts import render
from rest_framework import generics
from .serializer import QuestionSerializer
from myapp.models import Question


# Create your views here.
class QuestionAPIView(generics.ListCreateAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer