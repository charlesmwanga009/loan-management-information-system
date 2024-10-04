from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.home, name='home'),  # Add this line to handle the root URL
    path('leader/', views.leader, name='leader'),
    path('department/', views.department, name='department'),
    path('announcement/', views.announcement, name='announcement'),
    path('application/', views.application, name='application'),
]
