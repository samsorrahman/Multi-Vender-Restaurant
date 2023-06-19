
from django.urls import path, include
from . import views
from accounts import views as accountViews

urlpatterns = [
    path('', accountViews.vendorDashboard, name='vendor'),
    path('profile/', views.myprofile, name='myprofile'),
    path('menu_builder/', views.menu_builder, name="menu-builder"),
    path('menu_builder/category/<int:pk>/', views.fooditems_by_category, name='fooditems_by_category'),
    
    
     # Category CRUD
    path('menu_builder/category/add/', views.add_category, name='add_category'),
    path('menu_builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('menu_builder/category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    
    # Food Item CRUD
    path('menu_builder/food/add/', views.add_food, name='add_food'),
    path('menu_builder/food/edit/<int:pk>/', views.edit_food, name='edit_food'),
    path('menu_builder/food/delete/<int:pk>/', views.delete_food, name='delete_food'),
    
    
    
    # Opening Hour
    path('opening_hours/', views.opening_hours, name='opening_hours'),
    path('opening_hours/add/', views.add_opening_hours, name='add_opening_hours'),
]
