from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .models import (
    USWDSGraphicGrid,
    USWDSGraphicCard,
)

@plugin_pool.register_plugin
class USWDSGraphicCardPlugin(CMSPluginBase):
    allow_children = False
    module = _("Cards")
    name = _("Graphic card")
    require_parent = True
    model = USWDSGraphicCard

    change_form_template = "uswds/admin/change_form/admin-card-tabs.html"

    content = (
        _('Content'),
        {
            'fields': (
                'image',
                'title',
                'text',
            )
        }
    )

    fieldsets = (
        content,
    )

    def get_render_template(self, context, instance, placeholder):
        return f'uswds/content/graphic-list/uswds-graphic-card.html'

    def __unicode__(self):
        return self.name


@plugin_pool.register_plugin
class USWDSGraphicGridPlugin(CMSPluginBase):
    name = _("Graphic grid")
    model = USWDSGraphicGrid
    module = _("Graphic list")
    allow_children = True
    render_template = 'uswds/content/graphic-list/uswds-graphic-grid.html'
    child_classes = ['USWDSGraphicCardPlugin']

    def render(self, context, instance, placeholder):
        context = super(USWDSGraphicGridPlugin, self).render(context, instance, placeholder)
        return context