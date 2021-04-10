import requests
from django.conf import settings
from .models import EmailNews
from django.core.mail import EmailMultiAlternatives

API_KEY = settings.NEWS_API_KEY


def get_top_headlines_country(country_tag, source_tag, keyword_tag, request, page=1):
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
    user = request.user
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
                                p, created = EmailNews.objects.get_or_create(title=source['title'],
                                                                             user=user, send_status=True)
                                if created:
                                    html_context = f'<p><a href="{source["url"]}">{source["title"]}</a></p>'
                                    keyword_mail_list.append(html_context)
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
                        p, created = EmailNews.objects.get_or_create(title=source['title'],
                                                                     user=request.user, send_status=True)
                        if created:
                            html_context = f'<p><a href="{source["url"]}">{source["title"]}</a></p>'
                            keyword_mail_list.append(html_context)

    if keyword_mail_list:
        FORM_EMAIL = settings.FORM_EMAIL
        subject = 'News latter mail'
        text_content = '<p>This is an News latter message.<p>'
        html_content = ' <hr> '.join(keyword_mail_list)
        html_content = text_content + html_content
        msg = EmailMultiAlternatives(subject=subject, body=text_content, from_email=FORM_EMAIL, to=[str(user)])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    return headline_list, total_result
