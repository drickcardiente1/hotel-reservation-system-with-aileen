from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portal', views.portal, name='portal'),
    path('rooms', views.homeadmin, name='rooms'),
    path('procces', views.portalprocces, name='portalprocces'),
    path('procceslogout', views.procceslogout, name='procceslogout'),
    path('view/<int:g_id>/', views.view, name='view'),
    path('clear_procces', views.clear_procces, name='clear_procces'),
    path('delete_procces/<int:guest_id>/', views.delete_procces, name='delete_procces'),
]