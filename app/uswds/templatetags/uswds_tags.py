from django.template import Library

from filer.models import ThumbnailOption

register = Library()


@register.simple_tag
def get_thumbnail_option(name):
    option = ThumbnailOption.objects.filter(name=name).first()
    print(option.as_dict)
    return option.as_dict