from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Insurance
from insurance_clients_tracker.views import LoginRequiredView

from insurances.tables import InsuranceTable
from insurances.filter import InsuranceFilter

from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

class InsuranceListView(LoginRequiredView, SingleTableMixin, FilterView):
    model = Insurance
    template_name = 'insurance/insurance_list_table.html'
    context_object_name = 'insurances'
    table_class = InsuranceTable
    filterset_class = InsuranceFilter


# Detail view for displaying insurance details
class InsuranceDetailView(LoginRequiredView, DetailView):
    model = Insurance
    template_name = "insurance/insurance_detail.html"
    context_object_name = "insurance"


# Create view for adding a new insurance
class InsuranceCreateView(LoginRequiredView, CreateView):
    model = Insurance
    template_name = "insurance/insurance_form.html"
    fields = "__all__"  # You can customize the fields to be displayed
    success_url = reverse_lazy(
        "insurance_list"
    )  # Redirect to the insurance list view after successful creation


# Update view for editing insurance details
class InsuranceUpdateView(LoginRequiredView, UpdateView):
    model = Insurance
    template_name = "insurance/insurance_form.html"
    fields = "__all__"  # You can customize the fields to be displayed
    context_object_name = "insurance"
    success_url = reverse_lazy(
        "insurance_list"
    )  # Redirect to the insurance list view after successful update


# Delete view for deleting a insurance
class InsuranceDeleteView(LoginRequiredView, DeleteView):
    model = Insurance
    template_name = "insurance/insurance_confirm_delete.html"
    context_object_name = "insurance"
    success_url = reverse_lazy(
        "insurance_list"
    )  # Redirect to the insurance list view after successful deletion
