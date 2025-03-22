from django.urls import path
from . import views

app_name = 'AppRol'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin-dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('editar/', views.editar_articulo, name='editar_articulo'),
    path('ver/', views.ver_articulo, name='ver_articulo'),
]