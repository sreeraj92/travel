from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index.html', views.index, name='index_html'),
    path('hotel.html',views.hotel,name='hotel')
]
