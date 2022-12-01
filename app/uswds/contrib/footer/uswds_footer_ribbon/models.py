from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.uswds.models import USWDSLink


class SiteFooterRibbonLinks(CMSPlugin):
    def copy_relations(self, old_instance):
        self.footer_ribbon_link.all().delete()
        for footer_ribbon_link in old_instance.footer_ribbon_link.all():
            footer_ribbon_link.pk = None
            footer_ribbon_link.footer_ribbon_link = self
            footer_ribbon_link.save()

    def __unicode__(self):
        return _("Site Footer - Ribbon")

    def __str__(self):
        return "Site Footer - Ribbon"

    class Meta:
        verbose_name = _("Site Footer - Ribbon")


class SiteFooterRibbonLink(USWDSLink):
    footer_ribbon_link = models.ForeignKey(
        SiteFooterRibbonLinks,
        related_name="footer_ribbon_link",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        ordering = ['order']
