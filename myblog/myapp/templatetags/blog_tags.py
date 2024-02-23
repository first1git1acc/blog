#from django import template
from django.template.defaulttags import register
from myapp.models import Post
from django.template.defaultfilters import stringfilter

#register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.filter
def upp(value):
    return str(value).upper()