from django.urls import path, include
from . import views


urlpatterns = [
    path('taskgenerator/', views.TaskGeneratorAPIViews.as_view(), name='taskgenerator'),
    path('adminpage/', views.AdminAPIViews.as_view(), name='adminpage')
]