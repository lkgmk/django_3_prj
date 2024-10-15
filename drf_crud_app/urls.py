from django.urls import path
from .views import NameDetailsList, NameDetailsDetails

urlpatterns = [
    # path('names/', NameDetailsList.as_view(), name='name-list'),
    # path('names/<int:pk>', NameDetailsDetails.as_view(), name='name-details'),
    # path('name/new/<int:pk>', NameDetailView.as_view(), name='person-detail'),
    # path('name/new/<int:pk>/edit', NameUpdateView.as_view(), name='update-detail'),
    # path('name/new/<int:pk>/delete', NameDeleteView.as_view(), name='delete-detail'),
]
