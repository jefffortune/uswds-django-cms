from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


from uswds.models import USWDSLink


class USWDSHero(CMSPlugin):
    class Meta:
        verbose_name = _('USWDS Hero')

    background_image = FilerImageField(
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name="uswds_hero_background_image",
    )
    title_prefix = models.CharField(
        blank=True,
        help_text=_("Max length is 15 characters."),
        max_length=15,
        null=True,
    )
    title = models.CharField(
        blank=False,
        help_text=_("Max length is 60 characters."),
        max_length=60,
        null=False,
    )
    support = models.TextField(
        blank=True,
        help_text=_("Support the callout with some short explanatory text."),
        max_length=255,
        null=True,
    )

    align_support_choices = (
        ('support-left', "Left"),
        ('support-right', "Right"),
    )

    align_support = models.CharField(
        choices=align_support_choices,
        default='support-left',
        max_length=60,
    )

    def copy_relations(self, old_instance):
        self.uswds_hero_link.all().delete()
        for uswds_hero_link in old_instance.uswds_hero_link.all():
            uswds_hero_link.pk = None
            uswds_hero_link.uswds_hero_link = self
            uswds_hero_link.save()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class USWDSHeroLink(USWDSLink):
    class Meta:
        ordering = ['order']

    uswds_hero_link = models.ForeignKey(
        USWDSHero,
        on_delete=models.SET_NULL,
        related_name='uswds_hero_link',
        null=True,
    )

