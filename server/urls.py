
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from user.views import *
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.SimpleRouter()

# http://127.0.0.1:8000/api/userdata/
router.register(r'userdata', UserDataViewSet)

router.register(r'users', UsersViewSet)
router.register(r'userskills', UserSkillsViewSet)
router.register(r'userexperience', UserExperienceViewSet)

router.register(r'portfolio', PortfolioViewSet)
router.register(r'textfield', TextFieldViewSet)
router.register(r'link', LinkViewSet)
router.register(r'list', ListViewSet)
router.register(r'photo', PhotoViewSet)
router.register(r'slider', SliderViewSet)
router.register(r'sphere', SphereViewSet)
router.register(r'hashtag', HashtagViewSet)

router.register(r'portfoliobyuser', PortfolioGetByUserIdViewSet, basename='portfoliobyuser')
router.register(r'userdatabyuser', UserDataByUserIdViewSet, basename='userdatabyuser')
router.register(r'userskillsbyuser', UserSkillsByUserIdViewSet, basename='userskillsbyuser')
router.register(r'userexperiencebyuser', UserExperienceViewSet, basename='experiencebyuser')

urlpatterns = [ 
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('usersinfo/', UserInfoAllViewSet.as_view({'get': 'list'}), name='alluserinfo'),
    path('userinfo_username/<str:username>/', UserInfoViewSet.as_view({'get': 'list'}), name='userinfo'),
    path('users_by_username/<str:username>/', UsersViewSet.as_view({'get': 'list'}), name='user-detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), 
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'), 
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)