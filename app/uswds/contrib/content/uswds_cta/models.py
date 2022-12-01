from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField


from uswds.models import USWDSLink


class USWDSCTA(CMSPlugin):
    class Meta:
        abstract = True

    title = models.CharField(
        blank=True,
        max_length=255,
        null=True,
    )

    content = HTMLField(
        blank=True,
        configuration='CKEDITOR_SETTINGS_BASIC_TEXT',
        null=True,
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class USWDSCTAText(USWDSCTA):
    class Meta:
        verbose_name = _("USWDS CTA Text")

    name = _("USWDS CTA")
    # the key will be used part the template name.
    style_choices = (
        ('align', 'Aline'),
        ('stack', 'Stack'),
    )
    style = models.CharField(
        choices=style_choices,
        default='align',
        max_length=60,
    )

    def copy_relations(self, old_instance):
        self.uswds_cta_link.all().delete()
        for uswds_cta_link in old_instance.uswds_cta_link.all():
            uswds_cta_link.pk = None
            uswds_cta_link.uswds_cta_link = self
            uswds_cta_link.save()

    def __unicode__(self):
        return _(self.title)

    def __str__(self):
        return self.title


class USWDSCTATextLink(USWDSLink):
    class Meta:
        ordering = ['order']

    uswds_cta_link = models.ForeignKey(
        USWDSCTAText,
        on_delete=models.SET_NULL,
        related_name="uswds_cta_link",
        null=True,
    )