from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (
    USWDSCTAText,
    USWDSCTATextLink,
)


class CTALinkInline(admin.StackedInline):
    model = USWDSCTATextLink
    max_num = 1
    exclude = ['order']

@plugin_pool.register_plugin
class CTATextPlugin(CMSPluginBase):
    allow_children = False
    model = USWDSCTAText
    name = _("CTA Text")
    module = _("CTA")
    inlines = [CTALinkInline]
    text_enabled = True

    change_form_template = "uswds/admin/change_form/admin-cta-tabs.html"

    content = (
        _('Content'),
        {
            'fields': (
                'title',
                'content',
            )
        }
    )

    settings = (
        _('Settings'),
        {
            'fields': (
                'style',
            ),
            'classes': ['collapse']
        }
    )

    fieldsets = [
        content,
        settings,
    ]

    def render(self, context, instance, placeholder):
        context = super(CTATextPlugin, self).render(context, instance, placeholder)
        link = instance.uswds_cta_link.all()
        context.update({
            'link': link,
        })
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'inline_admin_formsets': [],
            'additional_formsets': context['inline_admin_formsets'],
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def get_render_template(self, context, instance, placeholder):
        return f'uswds/content/cta/uswds-text-{instance.style}.html'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
