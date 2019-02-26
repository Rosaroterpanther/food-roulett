from django.urls import path

from . import views

urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food/1234/
    path('<int:food_id>/', views.detail, name='detail'),
    # /food/add/
    path('add/', views.add, name='add'),

]
