from django import template

register = template.Library()

@register.filter
def attr(field, attrs):
    """Add attributes to a form field."""
    for attr in attrs.split():
        key, value = attr.split('=')
        field.field.widget.attrs[key] = value
    return field
