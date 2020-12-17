from django.urls import path
from .views import ComputerListView, ComputerUpdateView, ComputerCreateView, ComputerDeleteView, ComputerDetailView

urlpatterns = [
    path('', ComputerListView.as_view(), name='computer_list'),
    path('update/', ComputerUpdateView.as_view(), name='update_list'),
    path('create/', ComputerCreateView.as_view(), name='create_list'),
    path('<int:pk>/', ComputerDetailView.as_view(), name='detail_list'),
    path('delete/', ComputerDeleteView.as_view(), name='delete_from_list'),
]