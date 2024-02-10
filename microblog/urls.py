from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from blogapp.views import frontpage, post_detail

urlpatterns = [
    path('admin/', admin.site.urls), #URLがxxx.comの時，xxx.com/admin
    path("", frontpage),
    path("<slug:slug>/", post_detail, name="post_detail"), #xxx.com/{slug}とし，post_detailを返す(slugは投稿番号)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

