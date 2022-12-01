from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

class SiteFooterSocialModel(CMSPlugin):
    agency_logo = FilerImageField(
        null=True,
        blank=True,
        related_name="agency_logo_site_footer_social_model",
        on_delete=models.SET_NULL
    )
    agency_name = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )

    social_companies = [
        'facebook',
        'twitter',
        'youtube',
        'instagram',
        'rss'
    ]

    for social_company in social_companies:
        locals()[f'{social_company}_url'] = models.URLField(
            blank=True,
            max_length=255,
            null=True,
        )

    contact_title = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )

    contact_phone_label = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )

    contact_phone = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )

    contact_email_label = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )

    contact_email = models.EmailField(
        blank=True,
        max_length=255,
        null=True,
    )

    def __unicode__(self):
        return _(self.agency_name)

    def __str__(self):
        return "Site Footer - Agency"

    class Meta:
        verbose_name = _("Site Footer - Agency")
