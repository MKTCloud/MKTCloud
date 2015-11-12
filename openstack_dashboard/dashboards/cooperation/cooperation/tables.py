import logging
from django.utils.translation import ugettext_lazy as _

from horizon import tables
LOG = logging.getLogger(__name__)

class CreateInvite(tables.LinkAction):
    name = "invite"
    verbose_name = _("Create Invite")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")
    
class InviteAgain(tables.LinkAction):
    name = "again"
    verbose_name = _("Invite Again")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")    

class EditPermission(tables.LinkAction):
    name = "permission"
    verbose_name = _("Edit Permission")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")
    
class CancelInvite(tables.LinkAction):
    name = "more"
    verbose_name = _("Cancel Invite")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")    

class CooperationTable(tables.DataTable):
    id = tables.Column("id",verbose_name=_("ID"))
    username = tables.Column("username",verbose_name=_("Username"))
    email = tables.Column("email",verbose_name=_("Email"))
    roles = tables.Column("roles",verbose_name=_("Roles"))
    restate = tables.Column("restate",verbose_name=_("Restate"))
    time = tables.Column("time",verbose_name=_("Time"))
  
    class Meta:
      name = "cooperation"
      verbose_name = _("Cooperation") 
      table_actions = (CreateInvite, InviteAgain,EditPermission,CancelInvite)   