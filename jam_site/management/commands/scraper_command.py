from django.core.management.base import BaseCommand

from ._article_list_parser import parse_article_list
from ._feeds_parser import parse_feeds
from ._article_parser import parse_articles
from ._tagger import do_tagger
from ._shows_parser import parse_shows


class Command(BaseCommand):
    help = 'Scrapes articles and shows'

    def handle(self, *args, **kwargs):
        parse_article_list()
        self.stdout.write("parse_article_list done")
        parse_feeds()
        self.stdout.write("parse_feeds done")
        parse_articles()
        self.stdout.write("parse_articles done")
        do_tagger()
        self.stdout.write("do_tagger done")
        parse_shows()
        self.stdout.write("parse_shows done")
