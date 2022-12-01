from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .models import (
    USWDSHero,
    USWDSHeroLink,
)


class USWDSHeroLinkInline(admin.StackedInline):
    model = USWDSHeroLink
    max_num = 1
    exclude = ['order']


@plugin_pool.register_plugin
class USWDSHeroPlugin(CMSPluginBase):
    allow_children = False
    model = USWDSHero
    name = _("Hero")
    module = name
    inlines = [USWDSHeroLinkInline]

    change_form_template = "uswds/admin/change_form/admin-hero-tabs.html"
    render_template = "uswds/content/hero/uswds-hero.html"

    content = (
        _('Content'),
        {
            'fields': (
                'background_image',
                'title_prefix',
                'title',
                'support',
            )
        }
    )

    settings = (
        _('Settings'),
        {
            'fields': (
                'align_support',
            ),
            'classes': ['collapse']
        }
    )

    fieldsets = (
        content,
        settings,
    )

    def render(self, context, instance, placeholder):
        context = super(USWDSHeroPlugin, self).render(context, instance, placeholder)
        link = instance.uswds_hero_link.all()
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


    def __unicode__(self):
        return self.name
