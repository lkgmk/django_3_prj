from django.urls import path
from .views import NameCreateView, NameListView, \
    NameDetailView, NameUpdateView, NameDeleteView

urlpatterns = [
    path('', NameListView.as_view(), name='name-list'),
    # path('name/new/', NameCreateView.as_view(), name='create-view'),
    # path('name/new/<int:pk>', NameDetailView.as_view(), name='person-detail'),
    # path('name/new/<int:pk>/edit', NameUpdateView.as_view(), name='update-detail'),
    # path('name/new/<int:pk>/delete', NameDeleteView.as_view(), name='delete-detail'),

    path('createview', NameCreateView.as_view(), name='create-view'),
    path('detailview/<int:pk>', NameDetailView.as_view(), name='person-detail'),
    path('updateview/<int:pk>/edit', NameUpdateView.as_view(), name='update-detail'),
    path('deleteview/<int:pk>/delete', NameDeleteView.as_view(), name='delete-detail'),
]
