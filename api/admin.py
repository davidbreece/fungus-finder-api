from django.contrib import admin

# Register your models here.
from .models import Mushroom, WikiUrl
from .scraping import Scraper

admin.site.register(Mushroom)
admin.site.register(WikiUrl)

def get_links():
    with open("mycolinks.pickle", "rb") as f:
        links = pickle.load(f)
    return links


def get_urls(links):
    urls = []
    base = 'https://en.wikipedia.org'
    for key in links.keys():
        urls.append(base + links[key])
    return urls

