# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import logging
import os

import requests
from dateutil import parser
from dotenv import load_dotenv

from ...models import ArticleList, Article

conn = None
cursor = None
api_count = 0

load_dotenv()
ZYTE_KEY = os.getenv("ZYTE_KEY")
TM_API_KEY = os.getenv("TM_API_KEY")

logger = logging.getLogger(__name__)


def validate_string(val):
    try:
        if val != None:
            if type(val) is str:
                return val.encode('utf-8')
            else:
                return val
        if val != None:
            if type(val) is int:
                return str(val).encode('utf-8')
            else:
                return val
    except Exception as e:
        logger.error(e.strerror)


# do validation and checks before insert
def validate_date(val):
    try:
        if val != None:
            if type(val) is str:
                return parser.parse(val)
            else:
                return val
        if val != None:
            try:
                res = parser.parse(val)
                return res
            except ValueError:
                return None
    except Exception as e:
        logger.error(e.strerror)


def get_article(website_url):
    global api_count
    try:
        api_count += 1
        logger.debug('get_article with ' + website_url)
        response = requests.post('https://autoextract.scrapinghub.com/v1/extract',
                                 auth=(ZYTE_KEY, ''),
                                 json=[{'url': website_url, 'pageType': 'article'}],
                                 timeout=605)
        response_list = json.loads(response.text)
        if 'article' in response_list[0]:
            logger.debug('article in response_list[0]')
            logger.debug(response_list[0]['article'])
            return response_list[0]['article']
        else:
            logger.debug('article not in response_list[0]')
            return None
    except Exception as e:
        logger.error(e.strerror)
        return None


def parse_article(data):
    try:
        logger.debug('parse_article')
        article_body = None
        date_published_dt = None
        description = None
        headline = None
        url = None
        main_image = None

        if data != None:
            # is the key articleBody in the dict data?
            if 'articleBody' in data:
                # is the value of articleBody not None?
                if data['articleBody'] != None:
                    article_body = validate_string(data['articleBody'])

            if 'datePublished' in data:
                if data['datePublished'] != None:
                    date_published = validate_string(data['datePublished'])
                    date_published_dt = validate_date(date_published)

            if 'description' in data:
                if data['description'] != None:
                    description = validate_string(data['description'])

            if 'headline' in data:
                if data['headline'] != None:
                    headline = validate_string(data['headline'])
                    if headline != None:
                        if (len(headline) >= 1024):
                            headline = headline[0:1023]

            if 'url' in data:
                if data['url'] != None:
                    url = validate_string(data['url'])

            if 'mainImage' in data:
                if data['mainImage'] != None:
                    main_image = validate_string(data['mainImage'])
                    if main_image != None:
                        if (len(main_image) >= 1024):
                            main_image = None

            if (description != None and headline != None and url != None and main_image != None):
                logger.debug('insert into database')
                a_list = Article.objects.filter(url=url)

                if len(a_list) <= 0:
                    a = Article(date_published=date_published_dt, description=description, headline=headline, url=url,
                                main_image=main_image)
                    a.save()
    except Exception as e:
        logger.error(e.strerror)
        return None


def parse_articles():
    try:
        article_list = ArticleList.objects.filter(processed=False)
        for a in article_list:
            if api_count >= 10000:
                break

            article_dict = get_article(a.url)
            parse_article(article_dict)
            a.processed = True
    except Exception as e:
        logger.error(e.strerror)
        return None
