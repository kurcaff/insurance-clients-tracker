from django.urls import path
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, BirthdayClientsView

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('birthdays/', BirthdayClientsView.as_view(), name='birthday_view'),
]

    #TODO: Uncomment to include clients urls
    # path('clients/', include('clients.url')),
    # path('clients/', ClientListView.as_view(), name='client_list'),
    # path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    # path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    # path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    # path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),