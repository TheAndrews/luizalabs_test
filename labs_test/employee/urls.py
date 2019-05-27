from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path('employee/', views.EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', views.EmployeeDetailAPIView.as_view(), name='employee-detail'),
]