import logging
from django.utils.translation import ugettext_lazy as _

from horizon import tables
LOG = logging.getLogger(__name__)

class PendingAccept(tables.LinkAction):
    name = "pending"
    verbose_name = _("Pending Accept")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")
    
class Accepting(tables.LinkAction):
    name = "accepting"
    verbose_name = _("Accepting")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")    
 
class Resolved(tables.LinkAction):
    name = "resolved"
    verbose_name = _("Resolved")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")    
            
class Closed(tables.LinkAction):
    name = "closed"
    verbose_name = _("Closed")
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")    
    
class SupportTable(tables.DataTable):
    id = tables.Column("id",verbose_name=_("ID"))
    email = tables.Column("email",verbose_name=_("Email"))
    time = tables.Column("time",verbose_name=_("Time"))
  
    class Meta:
      name = "support"
      verbose_name = _("Support") 
      table_actions = (PendingAccept, Accepting,Resolved,Closed)  