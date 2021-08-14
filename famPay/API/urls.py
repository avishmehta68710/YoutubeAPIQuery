from django.urls import path
from . import views
from . import controller

urlpatterns = [
    path('index', views.index.as_view(), name='index'),
    path('search/<str:title>/<str:description>/',
         views.search, name='search'),
    path('addkey', views.AddAPIKey.as_view(), name='addkey'),
]

controller.THREAD.start()
