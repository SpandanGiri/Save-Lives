from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    path('',views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('NGO/', views.NGO,name='NGO'),
    path('NGO/funding', views.funding,name='funding'),
    path('NGO/contribute', views.contribute,name='contribute'),
    path('NGO/models/',views.suicide,name='suicide'),
    path('NGO/models/result',views.result,name='result'),
    path('survey',views.survey,name='survey'),
    path('tracker',views.tracker,name='tracker'),
    
    
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
