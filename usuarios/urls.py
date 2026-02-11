from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.cadastro, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('logout/', views.logout_view, name='logout'),
    path('acesso-recrutador/', views.login_recrutador, name='login_recrutador'),
]