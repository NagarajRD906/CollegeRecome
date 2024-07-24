from django.urls import path,include
from . import views
urlpatterns = [
	path('',views.homepage,name='home'),
	path('colleges/',views.college_list,name='colleges'),
	path('college/<str:pk>/',views.college_branch,name='college_branch'),
	path('college/<str:pk1>/<str:pk2>',views.college_branch_student,name='cbs'),
	path('colleges_link/', views.colleges_link, name='colleges_link'),
	path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]