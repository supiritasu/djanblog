from django.urls import path
from . import views

urlpatterns = [
    # 他のURLパターン
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('googled6cb1cfdea5ad30b.html/', views.google_search_console, name='google_search_console'),
]