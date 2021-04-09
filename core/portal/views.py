from django.http import HttpResponse

from .top_headlines import get_top_headlines_country


def get_top_headlines(request):
    json_value = get_top_headlines_country('country_tag', 'source_tag', 'keyword_tag', request)
    return HttpResponse(json_value)
