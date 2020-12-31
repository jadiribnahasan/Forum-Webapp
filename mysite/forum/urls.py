from django.urls import path, include
from . import views

app_name = "forum"

urlpatterns = [
    path('', views.forums, name='forums'),
    path('<int:pk>/', views.threads, name='threads'),
    path('create_forum/', views.create_forum, name='create_forum'),
    path('create_thread/<int:pk>', views.create_thread, name='create_thread'),
    path('thread<int:pk>/', views.thread_detail_view, name='thread_details'),
]
