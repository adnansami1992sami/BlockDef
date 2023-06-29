from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name="login.html"),name='login'),
	path('logout',views.user_logout,name='user_logout'),
	path('militarychief',views.militarychief_dashboard,name='militarychief_dashboard'),
	path('militarypersonal',views.militarypersonal_dashboard,name='militarypersonal_dashboard'),
	path('controlcenter',views.controlcenter_dashboard,name='controlcenter_dashboard'),
	path('user_login',views.user_login,name="user_login"),
	path('get_chief',views.get_chief,name="get_chief"),
	path('add_chief',views.add_chief,name='add_chief')
]