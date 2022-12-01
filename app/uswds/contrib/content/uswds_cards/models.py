from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


from uswds.models import USWDSLink


class USWDSCardBase(CMSPlugin):
    class Meta:
        verbose_name = _('USWDS Hero')
        abstract = True

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


class USWDSCard(USWDSCardBase):
    card_type_choices = (
        ('card', _("Card")),
        ('card-media', _("Card with media")),
        ('card-media-heading-first', _("Card with media heading first")),
        ('card-media-inset', _("Inset media")),
        ('card-media-exdent', _("Exdent media")),
    )

    card_type = models.CharField(
        choices=card_type_choices,
        default='card',
        max_length=60,
    )

    def copy_relations(self, old_instance):
        self.uswds_card_link.all().delete()
        for uswds_card_link in old_instance.uswds_card_link.all():
            uswds_card_link.pk = None
            uswds_card_link.uswds_card_link = self
            uswds_card_link.save()
    


class USWDSCardLink(USWDSLink):
    class Meta:
        ordering = ['order']

    uswds_card_link = models.ForeignKey(
        USWDSCard,
        on_delete=models.SET_NULL,
        related_name='uswds_card_link',
        null=True,
    )


class USWDSFlagCard(USWDSCardBase):
    card_type_choices = (
        ('card-flag', _("Default flag")),
        ('card-flag-right-inset', _("Flag media right inset"))
    )

    card_type = models.CharField(
        choices=card_type_choices,
        default='card',
        max_length=60,
    )

    def copy_relations(self, old_instance):
        self.uswds_flag_card_link.all().delete()
        for uswds_flag_card_link in old_instance.uswds_flag_card_link.all():
            uswds_flag_card_link.pk = None
            uswds_flag_card_link.uswds_flag_card_link = self
            uswds_flag_card_link.save()


class USWDSFlagCardLink(USWDSLink):
    class Meta:
        ordering = ['order']


    uswds_flag_card_link = models.ForeignKey(
        USWDSFlagCard,
        on_delete=models.SET_NULL,
        related_name='uswds_flag_card_link',
        null=True,
    )


class USWDSCardGrid(CMSPlugin):
    title = models.CharField(
        blank=False,
        max_length=255,
        null=False,
    )

    column_choices = (
        ('tablet:grid-col-6',_('Two Columns')),
        ('tablet:grid-col-4',_('Three Columns')),
        ('tablet:grid-col-3',_('Four Columns')),
    )

    columns = models.CharField(
        choices=column_choices,
        default='tablet:grid-col-3',
        max_length=60,
    )

    def __unicode__(self):
        return _(self.title)

    def __str__(self):
        return self.title
