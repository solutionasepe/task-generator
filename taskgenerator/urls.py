from django.urls import path, include
from . import views


urlpatterns = [
    path('taskgenerator/', views.TaskGeneratorAPIViews.as_view(), name='taskgenerator'),
    path('adminpage/', views.AdminAPIViews.as_view(), name='adminpage'),
    path('admindetail/<int:pk>/', views.AdminDetailsViews.as_view(), name='admindetail')
]