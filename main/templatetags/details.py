from django import template
from main.models import Number
register = template.Library()

@register.simple_tag
def get_obj(pk):
    kek = Number.objects.get(pk=pk)
    return (kek)