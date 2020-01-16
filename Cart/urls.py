from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.CartAPI.as_view(),name = "ayush"),
    path('items_all/<int:pk>/',views.Update.as_view()),

]