from django.conf.urls import url
import users.views as views


urlpatterns = [
	url(r'^$', views.check_login, name='check_login'),
	url(r'^app/user-dashboard/$', views.dashboard, name='dashboard'),
	url(r'^app/admin-dashboard/$', views.admin_dash, name='admin_dash'),
	url(r'^users/login/$', views.user_login, name='user_login'),
	url(r'^users/register/$', views.user_register, name='user_register'),
	url(r'^users/logout/$', views.quiz_logout, name='quiz_logout'),
]