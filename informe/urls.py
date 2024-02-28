from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from  . import views

router=routers.DefaultRouter()
router.register(r'informe',views.InformeViewSet)

urlpatterns =[
    path ('', views.index, name='index'),
    path(r'^', include(router.urls)),
    path(r'^api-auth',include('rest_framework.urls',namespace='rest_framework'))
]