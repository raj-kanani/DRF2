from django.urls import path
from .import views


urlpatterns = [
    # path('detail/<int:pk>/', views.detail, name='detail'),
    # path('list/', views.list, name='list'),
    # path('create/', views.student_create, name='create'),
    # path('api/', views.student_api, name='api'),
    path('Api/', views.StudentApi.as_view(), name='Api'),


]
