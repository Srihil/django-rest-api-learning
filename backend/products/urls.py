from django.urls import path
from . import views

urlpatterns = [
  path('',views.Product_List_Create_View, name='product-list'),
  path('<int:pk>/update/', views.Product_Update_View, name='product-edit'),
  path('<int:pk>/delete/', views.Product_delete_View),
  path('<int:pk>/', views.Product_Detail_View, name='product-detail'),
]