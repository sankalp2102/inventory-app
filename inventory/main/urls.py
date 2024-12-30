from django.urls import path
from .views import InventoryViewSet, RequestViewSet, TransactionViewSet ,LoginView

urlpatterns = [

    
    path('inventory/', InventoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='inventory-detail'),
    path('requests/', RequestViewSet.as_view({'get': 'list', 'post': 'create'}), name='request-list'),
    path('requests/<int:pk>/', RequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='request-detail'),
    path('transactions/', TransactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='transaction-detail'),
    path('auth/login/',LoginView.as_view(),name="login-user")
]