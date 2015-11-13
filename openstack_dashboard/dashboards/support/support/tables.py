import logging
from django.utils.translation import ugettext_lazy as _

from horizon import tables
LOG = logging.getLogger(__name__)

class PendingAccept(tables.LinkAction):
    name = "pending"
    verbose_name = _("Pending Accept")
    iconfont = "iconfont media-object"
    iconfontContent="1"
    card = "card card-blue"
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")
    
class Accepting(tables.LinkAction):
    name = "accepting"
    verbose_name = _("Accepting")
    iconfont = "iconfont media-object"
    iconfontContent="2"
    card = "card card-drank"
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")    
 
class Resolved(tables.LinkAction):
    name = "resolved"
    verbose_name = _("Resolved")
    iconfont = "iconfont media-object"
    iconfontContent="5"
    card = "card card-green"
    attrs={"data-toggle": "modal"}
    url = "#modalConfirm"
    classes = ("ajax-modal", "btn-create")    
            
class Closed(tables.LinkAction):
    name = "closed"
    verbose_name = _("Closed")
    iconfontContent="0"
    iconfont = "iconfont media-object"
    card = "card card-slategray"
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