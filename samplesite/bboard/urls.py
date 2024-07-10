from django.urls import path
from bboard import views

app_name = 'bboard'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('invalid_login_view/', views.invalid_login_view, name='invalid_login_view'),
    path('my_view/', views.my_view, name='my_view'),
]





