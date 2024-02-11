from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from blogapp.views import frontpage, post_detail, google_search_console

urlpatterns = [
    path('admin/', admin.site.urls), #URLがxxx.comの時，xxx.com/admin
    path("", frontpage),
    path("<slug:slug>/", post_detail, name="post_detail"), #xxx.com/{slug}とし，post_detailを返す(slugは投稿番号)
    path('googled6cb1cfdea5ad30b.html/', google_search_console, name='google_search_console'),
]

if settings.DEBUG != True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

