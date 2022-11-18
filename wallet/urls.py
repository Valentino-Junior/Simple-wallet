from django import urls
from .views import register,wallet,withdraw,deposit
from django.contrib.auth import views as auth_views

urlpatterns = [
    urls.path('', wallet, name='wallet'),
    urls.path('deposit', deposit, name='deposit'),
    urls.path('withdraw', withdraw, name='withdraw'),
    urls.path('register/', register, name='register'),
    urls.path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    urls.path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
