from apiapp import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register  ('songapi', views.SongListView )
router.register ('singerapi', views.SingerListView )

urlpatterns = [
    path('', include(router.urls))
    
]
