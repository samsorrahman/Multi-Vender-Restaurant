
from django.urls import path, include
from . import views
from accounts import views as accountViews

urlpatterns = [
    path('', accountViews.vendorDashboard, name='vendor'),
    path('profile/', views.myprofile, name='myprofile'),
    path('menu_builder/', views.menu_builder, name="menu-builder"),
    path('menu_builder/category/<int:pk>/', views.fooditems_by_category, name='fooditems_by_category'),
]
