import requests
from django.conf import settings
from user.utils import Util
from .models import News

API_KEY = settings.NEWS_API_KEY


def get_top_headlines_country(country_tag, source_tag, keyword_tag, request):
    if source_tag:
        source_list = [x.strip() for x in source_tag.split(',')]
    else:
        source_list = []
    if country_tag:
        country_list = [x.strip() for x in country_tag.split(',')]
    else:
        country_list = []
    if keyword_tag:
        keyword_list = [x.strip() for x in keyword_tag.split(',')]
    else:
        keyword_list = []

    headline_list = []
    keyword_mail_list = []
    for country in country_list:
        URL = f'https://newsapi.org/v2/top-headlines?country={country}&pageSize=20&apiKey={API_KEY}'
        req = requests.get(URL)
        req_value = req.json()
        get_sources = req_value['articles']
        for source in get_sources:
            source_name = source['source']

            if source_list:
                for key, value in source_name.items():
                    if value in source_list:
                        source['urlToImage'] = source['urlToImage'] if source['urlToImage'] else ''
                        headline_list.append(
                            News(user=request.user, headline=source['title'], thumbnail=source['urlToImage'],
                                 news_source=source['url'], country=country))
                        for keyword in keyword_list:
                            if keyword in source['title']:
                                keyword_mail_list.append(source['title'])
            else:
                source['urlToImage'] = source['urlToImage'] if source['urlToImage'] else ''
                headline_list.append(
                    News(user=request.user, headline=source['title'], thumbnail=source['urlToImage'],
                         news_source=source['url'], country=country))
                for keyword in keyword_list:
                    if keyword in source['title']:
                        keyword_mail_list.append(source['title'])

    if keyword_mail_list:
        data = {'email_body': keyword_mail_list[0], 'to_email': request.user,
                'email_subject': 'Reset your password'}
        Util.send_email(data)
    News.objects.bulk_create(
        headline_list
    )
    return headline_list
