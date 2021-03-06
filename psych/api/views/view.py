from django.http import JsonResponse
import json
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..models import profileDetail, Title, Answer, ok_Answer, Question, User, Results
from ..serializers import ProfileDetailSerializer,ResultSerializer, OkAnswerSerializer, TitleSerializer,TitleSerializer2, QuestionSerializer, UserSerializer, AnswerSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class profile(generics.ListCreateAPIView):
    queryset = profileDetail.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = (IsAuthenticated, )

class profiledetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = profileDetail.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = (IsAuthenticated, )

class okanswer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = OkAnswerSerializer

class results(generics.ListCreateAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultSerializer

class title(generics.ListAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAuthenticated, )

class user_reg(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class detailtitle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer2


class question(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # t = Question.objects.all()
    # serializer = QuestionSerializer(t, many=True)
    # if request.method == 'GET':
    #     return JsonResponse(serializer.data, safe=False)
    # return JsonResponse(serializer.errors)




class answer(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    # a = Answer.objects.all()
    # serializer = AnswerSerializer(a, many=True)
    # if request.method == 'GET':
    #     return JsonResponse(serializer.data, safe=False)
    # return JsonResponse(serializer.errors)
