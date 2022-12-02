from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .models import (
    USWDSCard,
    USWDSCardGrid,
    USWDSCardLink,
    USWDSFlagCard,
    USWDSFlagCardLink,
)


class USWDSCardBasePlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    module = _("Cards")
    require_parent = True

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

    settings = (
        _('Settings'),
        {
            'fields': (
                'card_type',
            ),
            'classes': ['collapse']
        }
    )

    fieldsets = (
        content,
        settings,
    )

    def get_render_template(self, context, instance, placeholder):
        return f'uswds/content/cards/uswds-card-{instance.card_type}.html'

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'inline_admin_formsets': [],
            'additional_formsets': context['inline_admin_formsets'],
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def __unicode__(self):
        return self.name


class USWDSCardGridBasePlugin(CMSPluginBase):
    class Meta:
        abstract = True

    model = USWDSCardGrid
    module = _("Cards")
    allow_children = True


@plugin_pool.register_plugin
class USWDSCardGrid(USWDSCardGridBasePlugin):
    name = _("Card grid")
    render_template = 'uswds/content/cards/uswds-card-grid.html'
    child_classes = ['USWDSCardPlugin']

    def render(self, context, instance, placeholder):
        context = super(USWDSCardGrid, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class USWDSFlagCardGrid(USWDSCardGridBasePlugin):
    name = _("Flag card grid")
    exclude = ['columns']
    render_template = 'uswds/content/cards/uswds-flag-card-grid.html'
    child_classes = ['USWDSFlagCardPlugin']
    css_class = "desktop:grid-col-6"

    exclude = ['columns']

    def render(self, context, instance, placeholder):
        context = super(USWDSFlagCardGrid, self).render(context, instance, placeholder)
        context.update({
            'css_class': self.css_class,
        })
        return context


class USWDSCardLinkInline(admin.StackedInline):
    model = USWDSCardLink
    max_num = 1
    exclude = ['order']


@plugin_pool.register_plugin
class USWDSCardPlugin(USWDSCardBasePlugin):
    model = USWDSCard
    name = _("Card")
    inlines = [USWDSCardLinkInline]
    parent_classes = []

    def render(self, context, instance, placeholder):
        context = super(USWDSCardPlugin, self).render(context, instance, placeholder)
        link = instance.uswds_card_link.all()
        context.update({
            'link': link,
        })
        return context


class USWDSFlagCardLinkInline(admin.StackedInline):
    model = USWDSFlagCardLink
    max_num = 1
    exclude = ['order']


@plugin_pool.register_plugin
class USWDSFlagCardPlugin(USWDSCardBasePlugin):
    model = USWDSFlagCard
    name = _("Flag Card")
    inlines = [USWDSFlagCardLinkInline]
    parent_classes = [
        'USWDSCardGridTwoCol',
    ]

    def render(self, context, instance, placeholder):
        context = super(USWDSFlagCardPlugin, self).render(context, instance, placeholder)
        link = instance.uswds_flag_card_link.all()
        context.update({
            'link': link,
        })
        return context
