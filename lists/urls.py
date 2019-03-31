from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:lists_id>/', views.detail, name='detail'),
    path('mycourses',views.mycourses,name='mycourses'),
    
    
    
    
]