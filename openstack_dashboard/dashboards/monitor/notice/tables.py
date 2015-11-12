import logging
from django.utils.translation import ugettext_lazy as _

from horizon import tables
LOG = logging.getLogger(__name__)

class CreateNotice(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Notice")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")
    
class UpdateNotice(tables.LinkAction):
    name = "update"
    verbose_name = _("Update Notice")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")

class DeleteNotice(tables.LinkAction):
    name = "delete"
    verbose_name = _("Delete Notice")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")
    
class NoticeTable(tables.DataTable):
    id = tables.Column("id",verbose_name=_("ID"))
    name = tables.Column("name",verbose_name=_("Name"))
    description = tables.Column("description",verbose_name=_("Description"))
    totalinvite = tables.Column("totalinvite",verbose_name=_("TotalInvite"))
    time = tables.Column("time",verbose_name=_("Time"))
  
    class Meta:
      name = "notice"
      verbose_name = _("Notice")    
      table_actions = (CreateNotice, UpdateNotice,DeleteNotice)