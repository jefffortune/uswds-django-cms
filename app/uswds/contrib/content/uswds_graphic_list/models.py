from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


from uswds.models import USWDSLink


class USWDSGraphicCard(CMSPlugin):
    class Meta:
        verbose_name = _('Graphic card')

    image = FilerImageField(
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
    )

    title = models.CharField(
        blank=False,
        help_text=_("Max length is 60 characters."),
        max_length=60,
        null=False,
    )

    text = models.TextField(
        blank=True,
        help_text=_("320 max character for a card description."),
        max_length=320,
        null=True,
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class USWDSGraphicGrid(CMSPlugin):
    class Meta:
        verbose_name = _('Graphic grid')

    title = models.CharField(
        blank=False,
        max_length=255,
        null=False,
    )

    def __unicode__(self):
        return _(self.title) if self.title else _("Graphic grid")

    def __str__(self):
        return self.title if self.title else "Graphic grid"