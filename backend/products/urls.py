from django.urls import path
from . import views

urlpatterns = [
  path('',views.product_mixin_view),
  path('<int:pk>/', views.Product_Detail_View),
  path('<int:pk>/update/', views.Product_Update_View),
  path('<int:pk>/delete/', views.Product_delete_View),
]