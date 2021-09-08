from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
   
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout' ),
    path('chatbot/',views.chatbot,name='chatbot'),
    
    
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)