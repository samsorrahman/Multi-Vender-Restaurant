
from django.urls import path, include
from . import views
from accounts import views as accountViews

urlpatterns = [
    path('', accountViews.vendorDashboard, name='vendor'),
    path('profile/', views.myprofile, name='myprofile')
]
