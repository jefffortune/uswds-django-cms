from cms.models.fields import PageField
from django.db import models
from django.utils.translation import gettext_lazy as _


class USWDSLink(models.Model):
    link_title = models.CharField(max_length=255)
    internal = PageField(
        blank=True,
        null=True,
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

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __unicode__(self):
        return _(self.link_title)

    def __str__(self):
        return self.link_title

    class Meta:
        abstract = True
