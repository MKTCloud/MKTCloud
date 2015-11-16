from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import messages
from horizon import tabs

from openstack_dashboard.api import keystone
from openstack_dashboard.api import network
from openstack_dashboard.api import nova

from .snapshots.tables import SnapshotsTable
from .volume_snapshots.tables import VolumeSnapshotsTable

class HostSnapshotTab(tabs.TableTab):
    table_classes = (SnapshotsTable,)
    name = _("Instance Snapshot")
    slug = "host_snapshot_tab"
    template_name = "horizon/common/_detail_table.html" 
    def get_snapshots_data (self):
       host=[]
       return host
    
class VolumeSnapshotTab(tabs.TableTab):
    table_classes = (VolumeSnapshotsTable,)
    name = _("Volume Snapshot")
    slug = "volume_snapshot_tab"
    template_name = "horizon/common/_detail_table.html"
    def get_volume_snapshots_data (self):
      volume=[]
      return volume 





class SnapshotTabs(tabs.TabGroup):
    slug = "snapshot_tabs"
    tabs = (HostSnapshotTab, VolumeSnapshotTab, )
    sticky = True
