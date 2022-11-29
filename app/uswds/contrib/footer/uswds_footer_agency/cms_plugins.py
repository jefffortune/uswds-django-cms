from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from adminsortable2.admin import SortableInlineAdminMixin

from .models import (
    SiteFooterAgencyMenuLinks,
    SiteFooterAgencyModel,
)



class SiteFooterAgencyMenuLinksInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    extra = 1
    model = SiteFooterAgencyMenuLinks

@plugin_pool.register_plugin
class SiteFooterAgencyPlugin(CMSPluginBase):
    allow_children = False
    model = SiteFooterAgencyModel
    module = _("Site Footer")

    inlines = (
        SiteFooterAgencyMenuLinksInlineAdmin,
    )

    change_form_template = "uswds/admin/change_form/admin-footer-agency-tabs.html"
    render_template = "uswds/footer/agency.html"

    agency = (
        _('Agency'),
        {
            'fields': (
                'agency_logo',
                'agency_name',
                'agency_domain',
                'agency_url',
            )
        }
    )

    services = (
        _('Services'),
        {
            'fields': (
                'services_description',
                'services_link_title',
                'services_link_url',
            ),
            'classes': ['collapsed']
        }
    )

    fieldsets = [
        agency,
        services,
    ]

    def render(self, context, instance, placeholder):
        context = super(SiteFooterAgencyPlugin, self).render(context, instance, placeholder)
        items = instance.footer_agency_menu_link.all()
        context.update({
            'items': items,
        })
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'inline_admin_formsets': [],
            'additional_formsets': context['inline_admin_formsets'],
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def __unicode__(self):
        return _("Site footer - Agency")

    def __str__(self):
        return "Site footer - Agency"
