from django.shortcuts import render
from rest_framework import generics, viewsets
from user.models import *
from user.permissions import IsOwnerOrReadOnly
from user.serializers import *


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = (IsOwnerOrReadOnly , )

class UserSkillsViewSet(viewsets.ModelViewSet):
    queryset = UserSkills.objects.all()
    serializer_class = UserSkillsSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserExperienceViewSet(viewsets.ModelViewSet):
    queryset = UserExperience.objects.all()
    serializer_class = UserExperienceSerializer  
    permission_classes = (IsOwnerOrReadOnly, )

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer 

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
     
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer 

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer 
     
class TextFieldViewSet(viewsets.ModelViewSet):
    queryset = TextField.objects.all()
    serializer_class = TextFieldSerializer  

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer  
    