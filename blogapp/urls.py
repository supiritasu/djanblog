from django.urls import path
from . import views

urlpatterns = [
    # 他のURLパターン
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
]
