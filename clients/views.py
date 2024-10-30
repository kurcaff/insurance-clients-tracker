from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import View
from django.utils import timezone
from datetime import timedelta

from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

from clients.models import Client
from clients.forms import ClientForm
from clients.tables import ClientTable
from clients.filter import ClientFilter

from insurance_clients_tracker.views import LoginRequiredView

# List view for displaying a list of clients
# class defined views
# class ClientListView(LoginRequiredView, ListView):
#     model = Client
#     template_name = "client/client_list.html"
#     context_object_name = "clients"
class ClientListView(LoginRequiredView, SingleTableMixin, FilterView):
    model = Client
    template_name = "client/client_list_table.html"
    #context_object_name = "clients"
    table_class = ClientTable
    filterset_class = ClientFilter

# Detail view for displaying client details
class ClientDetailView(LoginRequiredView, DetailView):
    model = Client
    template_name = "client/client_detail.html"
    context_object_name = "client"


class ClientDetailView(LoginRequiredView, DetailView):
    model = Client
    template_name = "client/client_detail.html"
    context_object_name = "client"

    def get(self, request, *args, **kwargs):
        client = self.get_object()
        form = ClientForm(instance=client)
        return render(request, self.template_name, {'client': client, 'form': form})


# # Create view for adding a new client
# class ClientCreateView(CreateView):
#     model = Client
#     template_name = "client/client_form.html"
#     fields = "__all__"  # You can customize the fields to be displayed
#     success_url = reverse_lazy(
#         "client_list"
#     )  # Redirect to the client list view after successful creation


# # Update view for editing client details
# class ClientUpdateView(UpdateView):
#     model = Client
#     template_name = "client/client_form.html"
#     fields = "__all__"  # You can customize the fields to be displayed
#     context_object_name = "client"
#     success_url = reverse_lazy(
#         "client_list"
#     )  # Redirect to the client list view after successful update
    
class ClientCreateView(LoginRequiredView, CreateView):
    model = Client
    form_class = ClientForm
    template_name = "client/client_form.html"
    success_url = reverse_lazy("client_list")

class ClientUpdateView(LoginRequiredView, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "client/client_form.html"
    context_object_name = "client"
    success_url = reverse_lazy("client_list")


# Delete view for deleting a client
class ClientDeleteView(LoginRequiredView, DeleteView):
    model = Client
    template_name = "client/client_confirm_delete.html"
    context_object_name = "client"
    success_url = reverse_lazy(
        "client_list"
    )  # Redirect to the client list view after successful deletion
    
class BirthdayClientsView(LoginRequiredView, View):
    template_name = 'client/birthday_clients.html'

    def get(self, request, *args, **kwargs):
        # Get today's date
        today = timezone.now().date()

        # Calculate yesterday and tomorrow
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)

        # Query clients with birthdays yesterday, today, and tomorrow (ignoring the year)
        clients_yesterday = Client.objects.filter(
            birthday__month=yesterday.month,
            birthday__day=yesterday.day
        )

        clients_today = Client.objects.filter(
            birthday__month=today.month,
            birthday__day=today.day
        )

        clients_tomorrow = Client.objects.filter(
            birthday__month=tomorrow.month,
            birthday__day=tomorrow.day
        )

        context = {
            'clients_yesterday': clients_yesterday,
            'clients_today': clients_today,
            'clients_tomorrow': clients_tomorrow,
        }

        return render(request, self.template_name, context)
