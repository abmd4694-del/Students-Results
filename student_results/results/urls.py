from django.urls import path
from . import views

urlpatterns = [
    # Home and authentication
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/<str:student_id>/', views.student_detail, name='student_detail'),
    path('students/create/new/', views.student_create, name='student_create'),
    path('students/<str:student_id>/edit/', views.student_edit, name='student_edit'),
    path('students/<str:student_id>/delete/', views.student_delete, name='student_delete'),
    
    # Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    
    # Result URLs
    path('results/create/', views.result_create, name='result_create'),
    path('results/<int:result_id>/edit/', views.result_edit, name='result_edit'),
    path('results/<int:result_id>/delete/', views.result_delete, name='result_delete'),
    path('results/search/', views.search_results, name='search_results'),
]
