from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin

app_name = "articles"
urlpatterns = [
    path('', views.articles_list,name="list"),
    path('<slug>',views.article_detail,name = "detail"),
]
