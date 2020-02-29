from django import template

register =template.Library()

@register.filter()
def set_goods_name(obj):
    return  obj[:100]+'...'
