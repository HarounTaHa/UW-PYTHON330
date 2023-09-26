from django.urls import path, include
from .views import list_view, detail_view

urlpatterns = [
    path('', list_view, name='poll_index'),
    path('polls/<int:poll_id>', detail_view, name='poll_detail'),

]
