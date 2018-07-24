from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register_user'),
    path('register/success.html', views.success_user_create, name='register_success'),

    path('profile/', views.profile, name='profile'),
    path('profile/update/<int:id>/', views.UpdateAccount.as_view(), name='account_update'),
]
