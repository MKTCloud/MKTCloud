from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.cooperation import dashboard


class Cooperation(horizon.Panel):
    name = _("Cooperation")
    slug = "cooperation"
    stylecss = 'iconfont icon-users'

dashboard.Cooperation.register(Cooperation)
