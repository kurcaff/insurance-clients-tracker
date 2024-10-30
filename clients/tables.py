import django_tables2 as tables
from .models import Client
from django.urls import reverse_lazy
from django.utils.html import format_html

class ClientTable(tables.Table):
    first_name = tables.Column(verbose_name="Name")
    last_name = tables.Column(verbose_name="Last Name")
    address = tables.Column(verbose_name="Address")
    region = tables.Column(empty_values=(), verbose_name="Region")
    phone_home = tables.Column(verbose_name="Phone Number")
    view = tables.Column(empty_values=(), verbose_name="View")

    def render_view(self, record):
        # Assuming you have a detail view for each client where you can also edit
        # Replace 'client_detail' with the name of your url pattern for the client detail view
        # 'record.pk' is the primary key of the client
        view_url = reverse_lazy('client_update', kwargs={'pk': record.pk})
        return format_html('<a href="{}">View/Edit</a>', view_url)

    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap.html"
        fields = ("first_name", "last_name", "address", "region", "phone_home", "view")

    def __init__(self, *args, **kwargs):
        super(ClientTable, self).__init__(*args, **kwargs)
        # Set 'view' column to use 'render_view' method for its content
        self.columns['view'].column.render = self.render_view
