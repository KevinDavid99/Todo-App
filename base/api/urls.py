from django.urls import path
from.import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.getRoutes),
    path('tasks/', views.get_task),
    path('tasks/<str:pk>/', views.getTask),
]


urlpatterns = format_suffix_patterns(urlpatterns)