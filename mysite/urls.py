from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.view import current_datetime,hello,hours_ahead,static_html,my_html,zhihu,worms,show
urlpatterns = patterns('view',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^sh/$',static_html),
    url(r'^my_html/$',my_html),
    url(r'^my_zhihu/$',zhihu),
    url(r'^worms/$',worms),
    url(r'^show/$',show),
)
