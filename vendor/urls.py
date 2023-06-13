
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
    # path('menu_builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    # path('menu_builder/category/delete/<int:pk>/', views.delete_category, name='delete_category'),

]
