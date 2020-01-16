from django.urls import path
from . import views
sd1 = (views.Standard.By_Search)
# sd2 = (views.Standard.Categories_API)
Im = (views.Immediate.By_Serach)
AD =(views.Advanced.By_Serach)

urlpatterns = [
    # path('home/',views.Product_API.as_view()),
    # path('by_name/<str:name>/',views.By_Serach.as_view()),
    # path('by_cate/<int:pk>/',views.Categories_API.as_view()),
    path('standard_all/',views.Standard.as_view()),
    path('standard_search/<str:name>/',sd1.as_view()),
    # path('standard_cate/', sd2.as_view()),

    path('immediate_all/', views.Immediate.as_view()),
    path('immediate_search/<str:name>/', Im.as_view()),

    path('advance_all/', views.Advanced.as_view()),
    path('advance_search/<str:name>/', AD.as_view()),

]