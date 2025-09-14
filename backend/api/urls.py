from django.urls import path
from .views import ProviderListAPIView, ProviderCreateAPIView, ProviderRetrieveUpdateAPIView

urlpatterns = [
    path('providers/', ProviderListAPIView.as_view(), name='providers-list'),
    path('providers/create/', ProviderCreateAPIView.as_view(), name='providers-create'),
    path('providers/<int:pk>/', ProviderRetrieveUpdateAPIView.as_view(), name='providers-detail-update'),
]
