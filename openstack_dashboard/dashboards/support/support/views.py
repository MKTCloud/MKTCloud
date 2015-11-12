import logging
from django.utils.translation import ugettext_lazy as _
from horizon import tables
from openstack_dashboard.dashboards.support.support import tables as project_tables
from horizon import views

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class =  project_tables.SupportTable
    template_name = 'support/support/index.html'

    def get_data(self):
        # Add data to the context here...
        resource = []
        return resource
