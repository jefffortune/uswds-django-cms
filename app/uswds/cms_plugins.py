import os.path


from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .models import (
    SiteFooterAgencyMenuLinks, 
    SiteFooterAgencyModel,
    SiteFooterSocialModel,
    SiteFooterLinkRibbonModel,
)


class SiteFooterAgencyMenuLinksInlineAdmin(admin.StackedInline):
    model = SiteFooterAgencyMenuLinks
    extra = 0


# Create your models here.
class SiteFooterAgencyPlugin(CMSPluginBase):
    model = SiteFooterAgencyModel
    module = _("Site Footer - Agency")
    inlines = (
        SiteFooterAgencyMenuLinksInlineAdmin,
    )

    render_template = "uswds/footer/site-footer-agency.html"
    
    def render(self, context, instance, placeholder):
        context = super(SiteFooterAgencyPlugin, self).render(context, instance, placeholder)
        return context
    
    def __unicode__(self):
        return _("Site footer - Agency")
    
    def __str__(self):
        return "Site footer - Agency"


class SiteFooterSocialPlugin(CMSPluginBase):
    model = SiteFooterSocialModel
    module_name = "Site Footer - Social"
    module = _(module_name)
    
    render_template = "uswds/footer/site-footer-agency.html"
    
    def __unicode__(self):
        return _(self.module_name)
    
    def __str__(self):
        return self.module_name


class SiteFooterLinkRibbonPlugin(CMSPluginBase):
    model = SiteFooterLinkRibbonModel
    module_name = "Site Footer - Social"
    module = _(module_name)
    
    render_template = "uswds/footer/site-footer-link--ribbon.html"
    
    def __unicode__(self):
        return _(self.module_name)
    
    def __str__(self):
        return self.module_name

plugin_pool.register_plugin(SiteFooterAgencyPlugin)
# plugin_pool.register_plugin(SiteFooterSocialPlugin)