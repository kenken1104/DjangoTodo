from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_for_user, name='home'),
    # path('post/', views.todos_for_user, name='home'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/delete/', views.TodoDeleteView.as_view(), name='post_delete'),
]
