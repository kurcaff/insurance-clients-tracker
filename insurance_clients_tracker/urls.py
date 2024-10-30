from django.contrib import admin
from django.urls import path, include
from .views import login_view, logout_view
from django.contrib.auth.views import LoginView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='clients/'), name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("admin/", admin.site.urls),
    path('clients/', include('clients.urls')),
    path('insurances/', include('insurances.urls')),
]
