
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('add/', views.add_task, name='add_task'),

    path('edit/<int:pk>/', views.edit_task, name='edit_task'),

    path('delete/<int:pk>/', views.delete_task, name='delete_task'),

    path('complete/<int:pk>/', views.complete_task, name='complete_task'),

    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='tasks/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(),
         name='logout'),path('api/tasks/', views.tasks_api, name='tasks_api'),
]

