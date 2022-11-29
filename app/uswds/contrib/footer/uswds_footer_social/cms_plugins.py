from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import SiteFooterSocialModel

@plugin_pool.register_plugin
class SiteFooterSocialPlugin(FrontendEditableAdminMixin, CMSPluginBase):
    allow_children = False
    model = SiteFooterSocialModel
    module_name = "Site Footer"
    module = _(module_name)

    frontend_editable_fields = ("agency_name")

    change_form_template = "djangocms_frontend/admin/base.html"
    render_template = "uswds/footer/social.html"

    agency = \
        (
            _("Agency"),
            {
                "fields": (
                    "agency_logo",
                    "agency_name",
                ),
            },
        )

    social = \
        (
            _("Social Companies"),
            {
                "fields": (
                    "facebook_url",
                    "twitter_url",
                    "youtube_url",
                    "instagram_url",
                    "rss_url",
                ),
                "classes": ['collapse',]
            },
        )

    contact = \
        (
            _("Contact Information"),
            {
                "fields": (
                    "contact_title",
                    "contact_phone_label",
                    "contact_phone",
                    "contact_email_label",
                    "contact_email",
                ),
                "classes": ['collapse', ]
            }

        )

    fieldsets = (
        agency,
        social,
        contact
    )

    def __unicode__(self):
        return _(self.module_name)

    def __str__(self):
        return self.module_name
