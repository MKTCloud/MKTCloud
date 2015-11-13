import logging

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import tables

from openstack_dashboard import api

class CreateCombinationAlarm(tables.LinkAction):
    name = "create"
    verbose_name = _("Create CombinationAlarm")
    card = "card card-blue"
    iconfont = "iconfont icon-drive media-object"
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")
    
class DeleteCombinationAlarm(tables.LinkAction):
    name = "delete"
    verbose_name = _("Delete CombinationAlarm")
    iconfont = "iconfont icon-delete media-object"
    card = "card card-red"
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")


class CombinationAlarmTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"))
    description = tables.Column("description", verbose_name=_("Description"))

    def sanitize_id(self, obj_id):
        return get_int_or_uuid(obj_id)
    
    class Meta:
        name = "combination_alarm"
        verbose_name = _("Combination Alarm")
        table_actions = (CreateCombinationAlarm, DeleteCombinationAlarm)
       