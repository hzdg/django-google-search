import math
from django.conf import settings
from django import template
from googlesearch import *

register = template.Library()


@register.inclusion_tag('googlesearch/_pagination.html', takes_context=True)
def show_pagination(context, pages_to_show=10):
    max_pages = int(math.ceil(context['total_results'] / results_per_page))
    last_page = int(context['current_page']) + pages_to_show - 1
    last_page = max_pages if last_page > max_pages else last_page
    prev_page = context['current_page'] - 1
    next_page = last_page + 1

    context.update({
        'pages': range(context['current_page'], last_page + 1),
        'prev_page': prev_page if context['current_page'] - 1 > 0 else 1,
        'next_page': next_page if next_page < max_pages else max_pages,
    })

    return context
