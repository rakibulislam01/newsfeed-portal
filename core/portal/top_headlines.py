import requests
from django.conf import settings
from user.utils import Util

API_KEY = settings.NEWS_API_KEY


def get_top_headlines_country(country_tag, source_tag, keyword_tag, page=1):
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
    total_result = 0
    for country in country_list:
        URL = f'https://newsapi.org/v2/top-headlines?country={country}&pageSize=10&page={page}&apiKey={API_KEY}'
        req = requests.get(URL)
        req_value = req.json()
        get_sources = req_value['articles']
        total_result = req_value['totalResults']
        for source in get_sources:
            source_name = source['source']

            if source_list:
                for key, value in source_name.items():
                    if value in source_list:
                        source['urlToImage'] = source['urlToImage'] if source['urlToImage'] else ''
                        news_data = {
                            'headline': source['title'],
                            'thumbnail': source['urlToImage'],
                            'news_source': source['url'],
                            'country': country
                        }
                        headline_list.append(news_data)
                        for keyword in keyword_list:
                            if keyword in source['title']:
                                keyword_mail_list.append(source['title'])
            else:
                source['urlToImage'] = source['urlToImage'] if source['urlToImage'] else ''
                news_data = {
                    'headline': source['title'],
                    'thumbnail': source['urlToImage'],
                    'news_source': source['url'],
                    'country': country
                }
                headline_list.append(news_data)
                for keyword in keyword_list:
                    if keyword in source['title']:
                        keyword_mail_list.append(source['title'])

    # if keyword_mail_list:
    #     data = {'email_body': keyword_mail_list[0], 'to_email': request.user,
    #             'email_subject': 'Reset your password'}
    #     Util.send_email(data)

    return headline_list, total_result
