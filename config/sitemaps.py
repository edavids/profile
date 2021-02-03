from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['about', 'home', 'contact', 'services', 'terms', 'privacy', 'cookies', 'works']

    def location(self, item):
        return reverse(item)
