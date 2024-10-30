import django_tables2 as tables
from .models import Insurance
from django.urls import reverse_lazy
from django.utils.html import format_html

class InsuranceTable(tables.Table):
    view = tables.Column(empty_values=())

    def render_view(self, record):
        # Assuming you have a detail view for each client where you can also edit
        # Replace 'client_detail' with the name of your url pattern for the client detail view
        # 'record.pk' is the primary key of the client
        view_url = reverse_lazy('insurance_update', kwargs={'pk': record.pk})
        return format_html('<a href="{}">View/Edit</a>', view_url)

    class Meta:
        model = Insurance
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "street", "zip_code", "view")

    def __init__(self, *args, **kwargs):
        super(InsuranceTable, self).__init__(*args, **kwargs)
        # Set 'view' column to use 'render_view' method for its content
        self.columns['view'].column.render = self.render_view
