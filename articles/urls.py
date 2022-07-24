from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<uuid:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
]