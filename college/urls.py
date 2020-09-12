from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from college import views
from django.views.generic.base import RedirectView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'notice',views.NoticeViewSet)
router.register(r'student',views.StudentViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('', RedirectView.as_view(url='api/')),
]