from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


@plugin_pool.register_plugin
class USWDSSideMenuPlugin(CMSPluginBase):
    render_template = 'uswds/menus/sidemenu.html'