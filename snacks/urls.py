from django.urls import path
from .views import SnackModelDetailView, SnackModelListView

urlpatterns = [
    path('', SnackModelListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackModelDetailView.as_view(), name='snack_detail'),
]
