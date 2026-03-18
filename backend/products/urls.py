from django.urls import path
from . import views

urlpatterns = [
  path('',views.Product_Create_View),
  path('<int:pk>/', views.Product_Detail_View)
]