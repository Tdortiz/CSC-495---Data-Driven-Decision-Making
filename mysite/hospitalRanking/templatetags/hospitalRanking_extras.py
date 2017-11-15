from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def phonenumber(value):
    print("____" + str(value))
    phone = '(%s) %s - %s' %(value[0:3], value[3:6], value[6:10])
    return phone
