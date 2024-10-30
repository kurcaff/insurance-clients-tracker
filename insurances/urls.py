from django.urls import path
from .views import InsuranceListView, InsuranceDetailView, InsuranceCreateView, InsuranceUpdateView, InsuranceDeleteView

urlpatterns = [
    path('', InsuranceListView.as_view(), name='insurance_list'),
    path('<int:pk>/', InsuranceDetailView.as_view(), name='insurance_detail'),
    path('create/', InsuranceCreateView.as_view(), name='insurance_create'),
    path('<int:pk>/update/', InsuranceUpdateView.as_view(), name='insurance_update'),
    path('<int:pk>/delete/', InsuranceDeleteView.as_view(), name='insurance_delete'),
]