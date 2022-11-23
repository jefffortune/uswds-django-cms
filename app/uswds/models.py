from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PageField
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

class SiteLink(models.Model):
    link_title = models.CharField(max_length=255)
    internal = PageField(
        blank=True,
        null=True
    )
    is_external = models.BooleanField(
        default=False,
        null=True,
    )
    external_url = models.URLField(
        blank=True,
        max_length=255,
        null=True,
    )
    
    def __unicode__(self):
        return _(self.link_title)
    
    def __str__(self):
        return self.link_title


class SiteFooterAgencyModel(CMSPlugin):
    site = Site.objects.get_current()
    agency_logo = FilerImageField(
        null=True,
        blank=True,
        related_name="agency_logo_site_footer_agency_model",
        on_delete=models.SET_NULL
    )
    agency_domain = models.CharField(
        blank=True,
        default=site.domain,
        max_length=255,
        null=True,
    )
    agency_name = models.CharField(
        blank=True,
        default=site.name,
        max_length=255,
        null=True,
    )
    agency_url = models.URLField(
        blank=True,
        default=site.domain,
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
    
    def copy_relations(self, oldinstance):
        # Before copying related objects from the old instance, the ones
        # on the current one need to be deleted. Otherwise, duplicates may
        # appear on the public version of the page
        self.associated_item.all().delete()

        for footer_agency_menu_link in oldinstance.footer_social_menu_link.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            footer_agency_menu_link.pk = None
            footer_agency_menu_link.plugin = self
            footer_agency_menu_link.save()
    
    def __unicode__(self):
        return _(self.agency_name)
    
    def __str__(self):
        return "Site Footer - Agency"


class SiteFooterAgencyMenuLinks(SiteLink):
    plugin = models.ForeignKey(
        SiteFooterAgencyModel,
        related_name="footer_agency_menu_link",
        on_delete=models.CASCADE,
        null=True,
    )


class SiteFooterSocialModel(CMSPlugin):
    site = Site.objects.get_current()
    agency_logo = FilerImageField(
        null=True,
        blank=True,
        related_name="agency_logo_site_footer_social_model",
        on_delete=models.SET_NULL
    )
    agency_name = models.CharField(
        blank=True,
        default=site.name,
        max_length=255,
        null=True,
    )
    

class SiteFooterLinkRibbonModel(CMSPlugin):
    pass