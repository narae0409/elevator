from django.urls import path
from . import views


app_name = 'elevator_api'
urlpatterns = [

    #Main
    path('data/', views.DataList.as_view()),
    path('data/address/', views.DataAddress.as_view()),
    path('data/insert/', views.DataInsert.as_view()),
    path('data/details/', views.Detail.as_view()),
    path('user/', views.NewUser.as_view()),
]

# path('data/<str:pk>/', views.DataDetail.as_view()),