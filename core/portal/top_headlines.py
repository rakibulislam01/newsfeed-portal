import requests
from django.conf import settings

API_KEY = settings.NEWS_API_KEY


def get_top_headlines_country():
    items = ['CNN', 'CNBC']
    country_list = ['us', 'jp']
    source_list = []
    for country in country_list:
        URL = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        req = requests.get(URL)
        req_value = req.json()
        get_sources = req_value['articles']
        for source in get_sources:
            source_name = source['source']
            for key, value in source_name.items():
                if value in items:
                    source_list.append(source)
    return source_list
