from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('cv-admin/', views.AdminView, name='admin'),
	path('cv-admin/addCurency/', views.AddCurrencyView, name='addCurency'),
	path('cv-admin/addCountry/', views.AddCountryView, name='addCountry'),
	path('cv-admin/update/<currency_id>/', views.update, name='update'),
	path('cv-admin/delete/<currency_id>/', views.delete, name='delete'),
	path('cv-admin/updateA/<country_id>/', views.update_c, name='update_c'),
	path('cv-admin/deleteV/<country_id>/', views.delete_c, name='delete_c'),
	path("login/", views.Connexion, name='login'),
	path("logout/", views.disconnect, name='logout'),
	path("register/", views.Register.as_view(), name='register'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),

]
