from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


from uswds.models import USWDSLink


class USWDSHeader(CMSPlugin):
    class Meta:
        verbose_name = _("USWDS Header")

    icon = FilerImageField(
        blank=True,
        help_text=_("Make sure the logo is sized appropriately for the space."),
        null=True,
        on_delete=models.SET_NULL,
    )

    name = models.CharField(
        blank=True,
        help_text=_("The name of the site or agency."),
        max_length=60,
        null=True,
    )

    show_search = models.BooleanField(
        default=True,
        help_text=_("Show the search bar in navigation."),
    )

    search_placeholder = models.CharField(
        default=_("Search..."),
        help_text=_("This text is included in the search input box as a placeholder. Max-length 60 characters."),
        max_length=60,
    )

    header_type_options = (
        ('default', _('Default dropdown')),
        ('mega_menu', _('Mega Menu'))
    )

    extended_header = models.BooleanField(
        default=False,
        help_text=_("An extended header allows for the inclusion of more sections in a horizontal navigation."),
    )

    header_type = models.CharField(
        choices=header_type_options,
        default='default',
        max_length=60,
    )
    
    def copy_relations(self, old_instance):
        self.uswds_action_link.all().delete()
        for uswds_action_link in old_instance.uswds_action_link.all():
            uswds_action_link.pk = None
            uswds_action_link.uswds_action_link = self
            uswds_action_link.save()

    def __unicode__(self):
        return _("USWDS Header")

    def __str__(self):
        return "USWDS Header"


class USWDSActionLink(USWDSLink):
    class Meta:
        ordering = ['order']

    uswds_action_link = models.ForeignKey(
        USWDSHeader,
        null=True,
        help_text=_("Will only display when extended menu is selected in settings tab."),
        on_delete=models.SET_NULL,
        related_name='uswds_action_link',
    )