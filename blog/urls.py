from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='listar_pub'),
    path('pub/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('pub/nuevo', views.nueva_pub, name='nueva_pub'),
    path('pub/<int:pk>/editar/', views.editar_pub, name='editar_pub'),
    path('bor/', views.listar_bor, name='listar_bor'),
    path('pub/<pk>/publicar/', views.publicar_pub, name='publicar_pub'),
    path('pub/<pk>/eliminar/', views.eliminar_pub, name='eliminar_pub'),
]
