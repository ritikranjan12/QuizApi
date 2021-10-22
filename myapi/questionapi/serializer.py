from myapp.models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question','option1','option2','option3','option4','answer')
