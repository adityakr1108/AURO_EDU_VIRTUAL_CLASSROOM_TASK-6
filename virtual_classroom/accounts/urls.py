from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView  # Importing the views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('video_chat/<str:room_name>/', views.video_chat_room, name='video_chat_room'), 
]
