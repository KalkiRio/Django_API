from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('dashboard/', views.dashboard_stats, name='dashboard-stats'),
]