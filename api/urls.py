from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('edit/<int:pk>', editar_company)
]