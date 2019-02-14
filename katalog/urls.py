from django.urls import path
from . import views

urlpatterns = [
    path('', views.Katalog, name='Katalog'),
    # path('db_blog/', views.db_blog, name='db_blog'),
    # path('new_post_blog/', views.input_post, name='input_post'),
]