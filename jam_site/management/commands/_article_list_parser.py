# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging
import os

import requests
from dotenv import load_dotenv
from requests import RequestException

from jam_site.models import ArticleList

jambase = [
    "https://jambands.com/category/news/",
    "https://liveforlivemusic.com/category/news/",
    "https://jambandnews.net/category/news/",
    "https://www.jambase.com/band/assembly-of-dust",
    "https://www.jambase.com/band/bela-fleck-and-the-flecktones",
    "https://www.jambase.com/band/ben-harper-the-innocent-criminals",
    "https://www.jambase.com/band/billy-strings",
    "https://www.jambase.com/band/blind-melon",
    "https://www.jambase.com/band/bruce-hornsby",
    "https://www.jambase.com/band/conspirator",
    "https://www.jambase.com/band/dark-star-orchestra",
    "https://www.jambase.com/band/dave-matthews-band",
    "https://www.jambase.com/band/dead-company",
    "https://www.jambase.com/band/dickey-betts-great-southern",
    "https://www.jambase.com/band/the-disco-biscuits",
    "https://www.jambase.com/band/dispatch",
    "https://www.jambase.com/band/donna-the-buffalo",
    "https://www.jambase.com/band/flowmotion",
    "https://www.jambase.com/band/g-love-special-sauce",
    "https://www.jambase.com/band/galactic",
    "https://www.jambase.com/band/garaj-mahal",
    "https://www.jambase.com/band/goose",
    "https://www.jambase.com/band/govt-mule",
    "https://www.jambase.com/band/guster",
    "https://www.jambase.com/band/hot-tuna",
    "https://www.jambase.com/band/jack-johnson",
    "https://www.jambase.com/band/joe-russos-almost-dead",
    "https://www.jambase.com/band/john-butler",
    "https://www.jambase.com/band/keller-williams",
    "https://www.jambase.com/band/leftover-salmon",
    "https://www.jambase.com/band/the-les-claypool-frog-brigade",
    "https://www.jambase.com/band/little-feat",
    "https://www.jambase.com/band/los-lonely-boys",
    "https://www.jambase.com/band/lotus",
    "https://www.jambase.com/band/matisyahu",
    "https://www.jambase.com/band/moe",
    "https://www.jambase.com/band/jj-grey-mofro",
    "https://www.jambase.com/search?q=My%20Morning%20Jacket",
    "https://www.jambase.com/band/new-monsoon",
    "https://www.jambase.com/band/nickel-creek",
    "https://www.jambase.com/band/o-a-r",
    "https://www.jambase.com/band/old-crow-medicine-show",
    "https://www.jambase.com/band/oysterhead",
    "https://www.jambase.com/band/particle",
    "https://www.jambase.com/band/pat-mcgee-band",
    "https://www.jambase.com/band/perpetual-groove",
    "https://www.jambase.com/band/phil-lesh-friends",
    "https://www.jambase.com/band/phish",
    "https://www.jambase.com/band/primus",
    "https://www.jambase.com/band/railroad-earth",
    "https://www.jambase.com/band/raq",
    "https://www.jambase.com/band/bob-weir-ratdog",
    "https://www.jambase.com/band/robert-randolph",
    "https://www.jambase.com/band/robert-walters-20th-congress",
    "https://www.jambase.com/band/signal-path",
    "https://www.jambase.com/band/sts9",
    "https://www.jambase.com/band/tedeschi-trucks-band",
    "https://www.jambase.com/band/the-bad-plus",
    "https://www.jambase.com/band/the-big-wu",
    "https://www.jambase.com/band/the-breakfast",
    "https://www.jambase.com/band/dirty-dozen-brass-band",
    "https://www.jambase.com/band/drive-by-truckers",
    "https://www.jambase.com/band/the-new-deal",
    "https://www.jambase.com/band/north-mississippi-allstars",
    "https://www.jambase.com/band/the-samples",
    "https://www.jambase.com/band/the-string-cheese-incident",
    "https://www.jambase.com/band/the-word",
    "https://www.jambase.com/band/trey-anastasio",
    "https://www.jambase.com/band/umphreys-mcgee",
    "https://www.jambase.com/band/victor-wooten",
    "https://www.jambase.com/band/ween",
    "https://www.jambase.com/band/widespread-panic",
    "https://www.jambase.com/band/yonder-mountain-string-band",
    "https://www.jambase.com/band/zilla",
    "https://antibalas.com/blog",
    "https://www.benharper.com/news",
    "https://www.billystrings.com/news",
    "https://www.brucehornsby.com/news-2",
    "https://www.darkstarorchestra.net/news",
    "https://dickeybetts.com/blog/",
    "https://www.fatfreddysdrop.com/news/",
    "https://galacticfunk.com/",
    "http://garajmahal.us/",
    "https://www.goosetheband.com/more-news",
    "https://mule.net/mulenews",
    "https://www.guster.com/#news",
    "https://jackjohnsonmusic.com/archive/news",
    "http://www.joerussosalmostdead.com/",
    "https://johnbutlertrio.com/news/",
    "https://lesclaypool.com/#anchor07",
    "https://www.mymorningjacket.com/news",
    "https://phish.com/news/",
    "http://primusville.com/#news",
    "https://railroad.earth/news/",
    "https://www.robertrandolph.net/news.html",
    "http://dirtydozenbrassband.com/news",
    "https://www.drivebytruckers.com/news.html",
    "https://www.stringcheeseincident.com/news/",
    "https://trey.com/news/",
    "https://www.umphreys.com/news/",
    "https://ween.com/",
    "https://widespreadpanic.com/news/",
    "https://www.yondermountain.com/news/",
    "https://www.alomusic.com/#news-section"
]

article_list = []
api_counter = 0

load_dotenv()
ZYTE_KEY = os.getenv("ZYTE_KEY")

logger = logging.getLogger(__name__)


def get_article_list(website_url):
    global api_counter
    if website_url != None:
        api_counter += 1
        try:
            response = requests.post(
                'https://autoextract.scrapinghub.com/v1/extract',
                auth=(ZYTE_KEY, ''),
                json=[{'url': website_url,
                       'pageType': 'articleList'}],
                timeout=605,
            )
        except RequestException as e:
            logger.error(e.strerror)
            return None

        logger.debug(response)
        return response.json()[0].get('articleList')


def parse_article_List(article_dict):
    try:
        if article_dict != None:
            if 'articles' in article_dict:
                for a in article_dict['articles']:
                    if 'url' in a:
                        article_list.append(a['url'])
    except Exception as e:
        logger.error(e.strerror)
    return


def parse_article_list():
    try:
        logger.debug("Starting article list scrape")
        for weburl in jambase:
            if api_counter >= 10000:
                break
            nextpage = True
            weburlNext = ''
            pagectr = 0
            while nextpage == True:
                logger.debug("Scraping: " + weburl + " pagectr = " + str(pagectr))
                article_dict = get_article_list(weburl)
                if article_dict != None:
                    parse_article_List(article_dict)
                    if article_dict.get('paginationNext'):
                        weburlNext = article_dict.get('paginationNext').get('url')
                        if weburl == weburlNext:
                            nextpage = False
                        else:
                            pagectr += 1
                            if pagectr > 5:
                                nextpage = False
                                pagectr = 0
                            weburl = weburlNext
                    else:
                        nextpage = False

            for url in article_list:
                qs = ArticleList.objects.filter(url=url)

                if len(qs) <= 0:
                    logger.debug("Inserting article url: " + url + " into database")
                    a = ArticleList(url=url, processed=False)
                    a.save()
            article_list.clear()
        logger.debug("Starting article list scrape")
        for weburl in jambase:
            if api_counter >= 10000:
                break
            nextpage = True
            weburlNext = ''
            pagectr = 0
            while nextpage == True:
                logger.debug("Scraping: " + weburl + " pagectr = " + str(pagectr))
                article_dict = get_article_list(weburl)
                if article_dict != None:
                    parse_article_List(article_dict)
                    if article_dict.get('paginationNext'):
                        weburlNext = article_dict.get('paginationNext').get('url')
                        if weburl == weburlNext:
                            nextpage = False
                        else:
                            pagectr += 1
                            if pagectr > 5:
                                nextpage = False
                                pagectr = 0
                            weburl = weburlNext
                    else:
                        nextpage = False

                else:
                    nextpage = False

            for url in article_list:
                qs = ArticleList.objects.filter(url=url)

                if len(qs) <= 0:
                    logger.debug("Inserting article url: " + url + " into database")
                    a = ArticleList(url=url, processed=False)
                    a.save()
            article_list.clear()
    except Exception as e:
        logger.error(e.strerror)
