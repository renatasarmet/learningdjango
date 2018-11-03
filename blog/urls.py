from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.initial, name='initial'),
    path('posts', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('clients', views.client_list, name='client_list'),
    path('client/new', views.client_new, name='client_new'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
