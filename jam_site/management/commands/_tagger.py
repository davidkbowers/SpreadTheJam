from ...models import Article, Band


def do_tagger():
    a_list = Article.objects.all()

    for a in a_list:
        tags = ""

        id = a.id
        print("tagging article id: " + str(id))

        description = a.description
        description_str = str(description)
        description_str = description_str.lower()

        headline = a.headline
        headline_str = str(headline)
        headline_str = headline_str.lower()

        bands = Band.objects.all()
        for band in bands:
            band_str = str(band)
            band_str = band_str.lower()

            if band_str in description_str or band_str in headline_str:
                tags += "#" + band_str
                band.tags = tags
                print()
                band.save()
