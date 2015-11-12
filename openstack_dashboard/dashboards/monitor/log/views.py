import logging
from django.utils.translation import ugettext_lazy as _
from horizon import tables
from openstack_dashboard.dashboards.monitor.log import tables as project_tables
from horizon import views

LOG = logging.getLogger(__name__)

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class =  project_tables.LogTable
    template_name = 'monitor/log/index.html'

    def get_data(self):
        # Add data to the context here...
        resource = []   
        return resource
