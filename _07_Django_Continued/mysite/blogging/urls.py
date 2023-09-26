from django.urls import path
from blogging.views import stub_view, list_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', stub_view, name="blog_detail"),
]
