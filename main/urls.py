from core.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('delete_task<int:task_id>/', views.delete_task, name="delete_task"),
    path('update_task<int:task_id>/', views.update_task, name="update_task"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('complete_task<int:task_id>/', views.complete_task, name='complete_task'),
    path('register/', views.register, name="register"),
    path('', views.user_login, name="user_login"),

]