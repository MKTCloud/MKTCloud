import logging

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard import api

class CreateAlarm(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Alarm")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")
    
class FilterAlarm(tables.LinkAction):
    name = "filter"
    verbose_name = _("Filter Alarm")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")

class MonitorIndicatorsTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"))
    description = tables.Column("description", verbose_name=_("Description"))

    def sanitize_id(self, obj_id):
        return get_int_or_uuid(obj_id)
    
    class Meta:
        name = "monitorin_dicators"
        verbose_name = _("Monitor Indicators")
        table_actions = (FilterAlarm, CreateAlarm)