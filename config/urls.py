from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.sitemaps.views import sitemap
from config.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    # 'awards':GenericSitemap({
    #     'queryset': Award.objects.all(),
    #     'date_field': 'updated',
    #     'issued_date': 'issued',
    # }, priority=0.9),
    # 'posts':GenericSitemap({
    #     'queryset': Post.objects.all_posts(),
    #     'date_field': 'updated',
    #     'pub_date': 'pub_date',
    # }, priority=0.9),
    # 'career':GenericSitemap({
    #     'queryset': Career.objects.all(),
    #     'date_field': 'updated',
    # }, priority=0.9),
}


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path("sentry-debug/", trigger_error),
    path("", include("favicon.urls")),
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path(
        "projects/",
        TemplateView.as_view(template_name="pages/construction.html"),
        name="works",
    ),
    # Privacy Policy and the rest
    path(
        "terms/", TemplateView.as_view(template_name="pages/terms.html"), name="terms"
    ),
    path(
        "policy/",
        TemplateView.as_view(template_name="pages/policy.html"),
        name="policy",
    ),
    path(
        "cookies/",
        TemplateView.as_view(template_name="pages/cookies.html"),
        name="cookies",
    ),
    path(
        "underconstruction/",
        TemplateView.as_view(template_name="pages/construction.html"),
        name="under-construction",
    ),
    # path('newsletter/', include('newsletter.urls')),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_FILEBROWSER_URL, site.urls),
    # path('grappelli/', include('grappelli.urls')),
    path("jet/", include("jet.urls", namespace="jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", namespace="jet-dashboard")),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path(settings.ADMIN_DOC_URL, include("django.contrib.admindocs.urls")),
    # User management
    path("users/", include("edavids.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("newsletter/", include("edavids.subscribe.urls", namespace="newsletter")),
    path("private/links/sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("tinymce/", include("tinymce.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

site.directory = "uploads/"