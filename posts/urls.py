from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='delete'),
    path('drafts/', views.DraftList.as_view(), name='post_draft_list'),
    path('<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='comment_delete'),
]
