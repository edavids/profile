from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'works', 'terms', 'policy', 'cookies']

    def location(self, item):
        return reverse(item)
