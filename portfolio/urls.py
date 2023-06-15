from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.home_page_view, name ='home'),
    path('blog', views.blog_page_view, name ='blog'),
    path('index', views.index_page_view, name='index'),
    path('escola', views.escola_page_view, name='escola'),
]