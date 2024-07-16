import logging
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from ...models import Band, Show

load_dotenv()
TM_API_KEY = os.getenv("TM_API_KEY")

logger = logging.getLogger(__name__)


def tm_fetch_concerts(band, start_date):
    try:
        logger.debug("fetching concerts for " + band)
        params = {'start_date.range_start': start_date, 'apikey': TM_API_KEY, 'keyword': band}
        response = requests.get(f"https://app.ticketmaster.com/discovery/v2/events.json?q=artist:{band}", params=params)
        concert_data = response.json()
    except Exception as e:
        logger.error(e.strerror)
        return None
    return concert_data


def tm_fetch_attractions(band):
    try:
        params = {'apikey': TM_API_KEY, 'keyword': band}
        response = requests.get(f"https://app.ticketmaster.com/discovery/v2/attractions.json-", params=params)
        concert_data = response.json()
    except Exception as e:
        logger.error(e.strerror)
        return None
    return concert_data


def parse_shows():
    try:
        bands = Band.objects.all()

        for b in bands:
            band_id = ""
            name = ""
            event_id = ""
            url = ""
            image_url = ""
            event_date = ""
            event_time = ""
            venue = ""
            city = ""
            state = ""
            country = ""

            band_id = b.id
            band_name = b.name

            start_date = datetime.today().strftime('%Y-%m-%d')
            concert_data = tm_fetch_concerts(band_name, start_date)

            if "_embedded" in concert_data:
                if "events" in concert_data['_embedded']:
                    events = concert_data['_embedded']['events']

                    for event in events:
                        if "name" in event:
                            name = event['name']
                        if "id" in event:
                            event_id = event['id']
                        if "url" in event:
                            url = event['url']
                        if "images" in event:
                            if len(event['images']) > 0:
                                if "url" in event['images'][0]:
                                    image_url = event['images'][0]['url']
                        if "dates" in event:
                            if "start" in event['dates']:
                                if "localDate" in event['dates']['start']:
                                    event_date = event['dates']['start']['localDate']
                                if "localTime" in event['dates']['start']:
                                    event_time = event['dates']['start']['localTime']
                        if "_embedded" in event:
                            if "venues" in event['_embedded']:
                                if len(event['_embedded']['venues']) > 0:
                                    if "name" in event['_embedded']['venues'][0]:
                                        venue = event['_embedded']['venues'][0]['name']
                                    if "city" in event['_embedded']['venues'][0]:
                                        if "name" in event['_embedded']['venues'][0]['city']:
                                            city = event['_embedded']['venues'][0]['city']['name']
                                    if "state" in event['_embedded']['venues'][0]:
                                        if "name" in event['_embedded']['venues'][0]['state']:
                                            state = event['_embedded']['venues'][0]['state']['name']
                                    if "country" in event['_embedded']['venues'][0]:
                                        if "name" in event['_embedded']['venues'][0]['country']:
                                            country = event['_embedded']['venues'][0]['country']['name']

                        if band_id == "":
                            band_id = None
                        if name == "":
                            name = None
                        if event_id == "":
                            event_id = None
                        if url == "":
                            url = None
                        if image_url == "":
                            image_url = None
                        if event_date == "":
                            event_date = None
                        if event_time == "":
                            event_time = None
                        if venue == "":
                            venue = None
                        if city == "":
                            city = None
                        if state == "":
                            state = None
                        if country == "":
                            country = None

                        s_list = Show.objects.filter(event_id=event_id, )

                        if len(s_list) <= 0:
                            s = Show(band_id=band_id, name=name, event_id=event_id, url=url, image_url=image_url,
                                     event_date=event_date, event_time=event_time, venue=venue, city=city, state=state,
                                     country=country)
                            s.save()
    except Exception as e:
        logger.error(e.strerror)
