from django.http import HttpResponse

from .top_headlines import get_top_headlines_country


def get_top_headlines(request):
    json_value = get_top_headlines_country()
    return HttpResponse(json_value)
