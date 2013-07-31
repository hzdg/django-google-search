import math
from django import template
from ..conf import settings

register = template.Library()


@register.inclusion_tag('googlesearch/_pagination.html', takes_context=True)
def show_pagination(context, pages_to_show=10):
    max_pages = int(math.ceil(context['total_results'] /
                              settings.GOOGLE_SEARCH_RESULTS_PER_PAGE))

    last_page = int(context['current_page']) + pages_to_show - 1
    last_page = max_pages if last_page > max_pages else last_page

    prev_page = context['current_page'] - 1
    next_page = context['current_page'] + 1

    context.update({
        'pages': range(1, max_pages + 1),
        'prev_page': prev_page if context['current_page'] - 1 > 0 else None,
        'next_page': next_page if next_page < max_pages else None,
    })

    return context
