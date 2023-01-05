from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .import views

app_name = 'compte'


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='compte/login.html',redirect_authenticated_user=True,authentication_form=LoginForm),name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/index.html',next_page='compte:login'),name="logout"),
    path('register/', views.register,name='register')

] 