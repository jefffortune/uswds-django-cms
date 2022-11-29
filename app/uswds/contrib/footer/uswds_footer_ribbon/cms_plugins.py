from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from adminsortable2.admin import SortableInlineAdminMixin

from .models import (
    SiteFooterRibbonLink,
    SiteFooterRibbonLinks,
)


class SiteFooterRibbonLinkInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    extra = 1
    model = SiteFooterRibbonLink


@plugin_pool.register_plugin
class SiteFooterRibbonPlugin(CMSPluginBase):
    allow_children = False
    model = SiteFooterRibbonLinks
    module = _("Site Footer")

    inlines = (
        SiteFooterRibbonLinkInlineAdmin,
    )

    change_form_template = "djangocms_frontend/admin/base.html"
    render_template = "uswds/footer/ribbon.html"

    def render(self, context, instance, placeholder):
        context = super(SiteFooterRibbonPlugin, self).render(context, instance, placeholder)
        items = instance.footer_ribbon_link.all()
        context.update({
            'items': items,
        })
        return context

    # def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
    #     context.update({
    #         'inline_admin_formsets': [],
    #         'additional_formsets': context['inline_admin_formsets'],
    #     })
    #     return super().render_change_form(request, context, add, change, form_url, obj)

    def __unicode__(self):
        return _("Site footer - Ribbon Links")

    def __str__(self):
        return "Site footer - Ribbon Links"
