from django.conf.urls import url, include
from . import views # '.' signifies current directory

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^submit', views.submit, name='summarise')
	]
