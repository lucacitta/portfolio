
from django.contrib import admin
from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('homeEn',views.homeEn,name='homeEn'),
]
