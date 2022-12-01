from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


from uswds.models import USWDSLink


class SiteFooterAgencyModel(CMSPlugin):
    agency_logo = FilerImageField(
        null=True,
        blank=True,
        related_name="agency_logo_site_footer_agency_model",
        on_delete=models.SET_NULL
    )
    agency_domain = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )
    agency_name = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )
    agency_url = models.URLField(
        blank=True,
        max_length=255,
        null=True,
    )
    services_description = models.TextField(
        blank=True,
        null=True,
    )
    services_link_title = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )
    services_link_url = models.URLField(
        blank=True,
        null=True,
    )

    def copy_relations(self, old_instance):
        self.footer_agency_menu_link.all().delete()
        for footer_agency_menu_link in old_instance.footer_agency_menu_link.all():
            footer_agency_menu_link.pk = None
            footer_agency_menu_link.footer_agency_menu_link = self
            footer_agency_menu_link.save()

    def __unicode__(self):
        return _(self.agency_name)

    def __str__(self):
        return "Site Footer - Agency"

    class Meta:
        verbose_name= _( "Site Footer - Agency")


class SiteFooterAgencyMenuLinks(USWDSLink):
    footer_agency_menu_link = models.ForeignKey(
        SiteFooterAgencyModel,
        related_name="footer_agency_menu_link",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        ordering = ['order']
