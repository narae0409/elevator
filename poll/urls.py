from django.urls import path
from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name='idx'),
    path('get/', views.index_GET, name='idx_get'),
    path('post/', views.index_POST, name='idx_post'),
    path('post/search/', views.index_Search, name='idx_SR'),
    path('search/', views.index_Search, name='idx_SR'),
    path('tables/', views.index_Tables, name='idx_TB'),
    path('address/', views.index_Address, name='idx_AR'),
    path('main/number/', views.index_NumberMain, name='idx_NBM'),
    path('main/number/day/', views.index_NumberMain_D, name='idx_NBMD'),
    path('main/number/week/', views.index_NumberMain_W, name='idx_NBMW'),
    path('main/number/month/', views.index_NumberMain_A, name='idx_NBMA'),
    path('api/graph/', views.ElvtAPIVIEW_T.as_view(), name="idx_APIT"),
    path('api/graph/day/', views.ElvtAPIVIEW_D.as_view(), name="idx_APID"),
    path('api/graph/week/', views.ElvtAPIVIEW_W.as_view(), name="idx_APIW"),
    path('api/graph/month/', views.ElvtAPIVIEW_A.as_view(), name="idx_APIA"),
    path('graph/', views.index_GraphT, name='idx_GPT'),
    path('graph/day/', views.index_GraphD, name='idx_GPD'),
    path('graph/week/', views.index_GraphW, name='idx_GPW'),
    path('graph/month/', views.index_GraphA, name='idx_GPA'),
    path('graphic/', views.index_Graphic, name='idx_GRP'),
    path('blogMain/', views.blogMain, name='blogMain'),
    path('blogS/', views.blogS, name='blogS'),
]