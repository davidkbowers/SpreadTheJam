import feedparser

from ...models import ArticleList


def parse_feeds():
    rows = ['https://jambands.com/feed/',
            'https://rss2.feedspot.com/https://jammagazine.com/',
            'https://rss2.feedspot.com/https://www.holidayatthesea.com/music/tag/jam',
            'https://jambandnews.net/feed/',
            'https://www.thejamwich.com/feed/',
            'https://jambands.com/feed/',
            'https://consequence.net/tag/jam-band/feed/',
            'https://www.jambandpurist.com/1/feed',
            'http://feeds.feedburner.com/LeewaysHomeGrownMusicNetwork',
            'https://hookjams.com/blog-2/feed/',
            'https://www.jambase.com/feed',
            'https://rockcellarmagazine.com/tag/jam-band/feed/',
            'https://rss2.feedspot.com/https://phish.com/news/',
            'https://www.goldminemag.com/tag/jam-bands?',
            'https://rss2.feedspot.com/https://jammagazine.com/']

    print("running feedparser")

    try:
        for row in rows:
            link = row
            print("parsing " + link)
            feed = feedparser.parse(link)
            for entry in feed.entries:
                if 'link' in entry:
                    link = entry.link
                else:
                    link = None

                if link != None:
                    qs = ArticleList.objects.filter(url=link)

                    if len(qs) <= 0:
                        print("Inserting article url: " + link + " into database")
                        a = ArticleList(url=link, processed=False)
                        a.save()

    finally:
        print("finished")
