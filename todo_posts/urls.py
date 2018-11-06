from django.urls import path
from django_filters.views import FilterView
from todo_posts.filters import Todo_postFilter
from . import views


urlpatterns = [
    path('', views.Todo_postListView.as_view(), name='todo_post_list'),
    path('<int:pk>/edit/', views.Todo_postUpdateView.as_view(), name='todo_post_edit'),
    path('<int:pk>/', views.Todo_postDetailView.as_view(), name='todo_post_detail'),
    path('<int:pk>/delete/', views.Todo_postDeleteView.as_view(), name='todo_post_delete'),
    path('new/', views.Todo_postCreateView.as_view(), name='todo_post_new'),
    path('search/', FilterView.as_view(filterset_class=Todo_postFilter,
        template_name='todo_post_filter.html'), name='search'),
]
