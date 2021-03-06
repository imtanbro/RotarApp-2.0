from django.urls import path, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.home1, name = 'main_home'),
    path('home/', views.home1, name = 'main_home1'),
    path('aboutUs/', views.aboutUs, name = 'main_aboutUs'),
    path('eRyla/', views.eRyla, name = 'main_eRyla'),
    path('council/', views.council, name = 'main_council'),
    path('whatWeDo/', views.whatWeDo, name = 'main_whatWeDo'),
    path('resources/', views.resources, name = 'main_resources'),
    url(r'^document/(?P<document>.+?)/$', views.document, name='main_document'),
       
]
