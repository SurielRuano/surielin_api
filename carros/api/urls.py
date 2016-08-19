from django.conf.urls import url
from . import views

urlpatterns =[


url(r'^carros/$',views.CarroListView.as_view(),name='carro_lists'),

url(r'^carros/(?P<pk>\d+/)$',views.CarroListView.as_view(),name = 'carro_detail'),
	


]