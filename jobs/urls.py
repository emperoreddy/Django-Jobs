from django.urls import path
from jobs import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JobView.as_view(), name='list_jobs'),
    path('new/', views.CreateJobView.as_view(), name='create_job'),
    path('<int:pk>/edit/', views.UpdateJobView.as_view(), name='edit_job'),
    path('<int:pk>/activate/', views.activate, name='activate'),
    path('<int:pk>/deactivate/', views.deactivate, name='deactivate'),
    path('<int:pk>/delete', views.DeleteJobView.as_view(), name='delete'),
]
