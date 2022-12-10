from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .models import (
    USWDSHeader,
    USWDSActionLink,
)


class USWDSHeaderLinkInline(admin.StackedInline):
    model = USWDSActionLink
    max_num = 5
    extra = 0
    exclude = ['order']



@plugin_pool.register_plugin
class USWDSHeaderPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    cache = False
    inlines = [USWDSHeaderLinkInline]
    model = USWDSHeader
    module = _("Header")
    name = _("USWDS Header")

    change_form_template = "uswds/admin/change_form/admin-header-tabs.html"

    site_identity = (
        _('Site identity'),
        {
            'fields': (
                'icon',
                'name',
            )
        }
    )

    search = (
        _('Search'),
        {
            'fields': (
                'show_search',
                'search_placeholder'
            ),
            'classes': ['collapse']
        }
    )

    settings = (
        _('Settings'),
        {
            'fields': (
                'extended_header',
                'header_type',
            ),
            'classes': ['collapse']
        }
    )

    fieldsets = (
        site_identity,
        search,
        settings,
    )

    def get_render_template(self, context, instance, placeholder):
        return f'uswds/header/uswds-header.html' if not instance.extended_header else f'uswds/header/uswds-extended-header.html'

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'inline_admin_formsets': [],
            'additional_formsets': context['inline_admin_formsets'],
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def __str__(self):
        return self.name