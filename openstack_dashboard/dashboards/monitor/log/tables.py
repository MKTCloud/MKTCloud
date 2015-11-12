import logging
from django.utils.translation import ugettext_lazy as _

from horizon import tables
LOG = logging.getLogger(__name__)


class LogTable(tables.DataTable):
    id = tables.Column("id",verbose_name=_("ID"))
    name = tables.Column("name",verbose_name=_("Name"))
    operation = tables.Column("Operation",verbose_name=_("Operation"))
    state = tables.Column("State",verbose_name=_("State"))
    operationTime = tables.Column("operationtime",verbose_name=_("OperationTime"))
    time = tables.Column("time",verbose_name=_("Time"))
  
    class Meta:
      name = "notice"
      verbose_name = _("Notice")    
 