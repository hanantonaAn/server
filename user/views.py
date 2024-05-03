from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import *
from user.permissions import *
from user.serializers import *

class FetchVacanciesView(APIView):
    def get(self, request):
        username = self.request.query_params.get('username', None)
        if username is None:
            return Response({"error": "Username parameter is required."}, status=400)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)
        
        fetch_and_save_vacancies(username)
        
        return Response({"message": "Вакансии успешно получены и сохранены."})

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = UserVacancy.objects.all()
    serializer_class = VacancySerializer  
    permission_classes = (IsOwnerOrReadOnly, )

    # def get_queryset(self):
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         return UserVacancy.objects.filter(user__username=username)

class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    # permission_classes = (IsOwnerOrReadOnly,  )

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is None:
            username = self.kwargs.get('username', None)
        
        if username is not None:
            return User.objects.filter(username=username)
        
        return User.objects.all()   

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def list(self, request, username=None):
        user = User.objects.filter(username=username).get()
        user_data = UserData.objects.filter(user_id=user.id).first()
        user_skills = UserSkills.objects.filter(user_id=user.id).first()
        user_exp = UserExperience.objects.filter(user_id=user.id).all()
        user_portfolio = Portfolio.objects.filter(user_id=user.id).first()

        user_serializer = UsersSerializer(user)
        user_data_serializer = DataSerializer(user_data) if user_data else None
        user_skills_serializer = UsersSkillsSerializer(user_skills) if user_skills else None
        
        # Убедитесь, что user_exp_serializer возвращает список
        user_exp_serializer = UsersExpSerializer(user_exp, many=True) if user_exp else None
        
        user_portfolio_serializer = UsersPortSerializer(user_portfolio) if user_portfolio else None

        data = {
            'user': user_serializer.data,
            'user_data': user_data_serializer.data if user_data_serializer else None,
            'user_skills': user_skills_serializer.data if user_skills_serializer else None,
            'user_experience': user_exp_serializer.data if user_exp_serializer else None,
            'user_portfolio': user_portfolio_serializer.data if user_portfolio_serializer else None,
        }

        return Response(data)

    
class UserInfoAllViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        users = User.objects.all()
        user_data = UserData.objects.all()
        user_skills = UserSkills.objects.all()
        user_exp = UserExperience.objects.all()
        user_portfolio = Portfolio.objects.all()

        aggregated_data = []

        for user in users:
            user_info = {
                'user': UsersSerializer(user).data,
                'user_data': DataSerializer(user_data.filter(user_id=user.id), many=True).data,
                'user_skills': UsersSkillsSerializer(user_skills.filter(user_id=user.id), many=True).data,
                'user_experience': UsersExpSerializer(user_exp.filter(user_id=user.id), many=True).data,
                'user_portfolio': UsersPortSerializer(user_portfolio.filter(user_id=user.id), many=True).data,
            }
            aggregated_data.append(user_info)

        return Response(aggregated_data) 
    
class PublicUserInfoAllViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        users = User.objects.all()
        user_data = UserData.objects.all()
        user_skills = UserSkills.objects.all()
        user_exp = UserExperience.objects.all()
        user_portfolio = Portfolio.objects.filter(public=True)

        aggregated_data = []

        for user in users:
            user_info = {
                'user': UsersSerializer(user).data,
                'user_data': DataSerializer(user_data.filter(user_id=user.id), many=True).data,
                'user_skills': UsersSkillsSerializer(user_skills.filter(user_id=user.id), many=True).data,
                'user_experience': UsersExpSerializer(user_exp.filter(user_id=user.id), many=True).data,
                'user_portfolio': UsersPortSerializer(user_portfolio.filter(user_id=user.id), many=True).data,
            }
            aggregated_data.append(user_info)

        return Response(aggregated_data)     

class UserDataByUserIdViewSet(viewsets.ModelViewSet):
    serializer_class = UserDataSerializer
    def get_queryset(self):
        return UserData.objects.filter(user_id=self.request.user)    

class UserSkillsViewSet(viewsets.ModelViewSet):
    queryset = UserSkills.objects.all()
    serializer_class = UserSkillsSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class UserSkillsByUserIdViewSet(viewsets.ModelViewSet):
    serializer_class = UserSkillsSerializer
    def get_queryset(self):
        return UserSkills.objects.filter(user_id=self.request.user)     

class UserExperienceViewSet(viewsets.ModelViewSet):
    queryset = UserExperience.objects.all()
    serializer_class = UserExperienceSerializer  
    permission_classes = (IsOwnerOrReadOnly, )

class UserExperienceByUserIdViewSet(viewsets.ModelViewSet):
    serializer_class = UserExperienceSerializer
    def get_queryset(self):
        return UserExperience.objects.filter(user_id=self.request.user)  
       

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer 

class PortfolioGetByUserIdViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioByUserIdSerializer
    def get_queryset(self):
        return Portfolio.objects.filter(user_id=self.request.user)  

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
     
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer 

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer 

class HeadingViewSet(viewsets.ModelViewSet):
    queryset = Heading.objects.all()
    serializer_class = HeadingSerializer
     
class TextFieldViewSet(viewsets.ModelViewSet):
    queryset = TextField.objects.all()
    serializer_class = TextFieldSerializer  

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer  

class SliderImageViewSet(viewsets.ModelViewSet):
    queryset = SliderImage.objects.all()
    serializer_class = SliderImageSerializer  

class GetImagesBySliderRequest(APIView):
    serializer_class = SliderImageSerializer

    def get(self, request):
        slider_id = request.query_params.get('slider_id', None)
        if slider_id is None:
            return Response({"error": "Slider id parameter is required."}, status=400)
        
        try:
            slider = Slider.objects.get(id=slider_id)
        except Slider.DoesNotExist:
            return Response({"error": "Slider not found."}, status=404)
        
        images = SliderImage.objects.filter(slider_id=slider)
        serializer = SliderImageSerializer(images, many=True)  
        
        return Response(serializer.data)
  
class SphereViewSet(viewsets.ModelViewSet):
    queryset = Sphere.objects.all()
    serializer_class = SphereSerializer  

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer    
    
   