from django.urls import path
from .views import JerseyList
from .views import JerseyListCreateView, JerseyDetailView
urlpatterns = [
    path('jerseys/', JerseyList.as_view(), name='jersey-list'),
    path('jerseys/<int:pk>/', JerseyDetailView.as_view(), name='jersey-detail'),
]
