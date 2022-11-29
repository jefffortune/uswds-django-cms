from django import template

register = template.Library()

@register.filter
def get_dict_value(dict, key):
    if key in dict:
        return dict[key]
    else:
        return False