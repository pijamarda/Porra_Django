from django.conf.urls import patterns, include, url

from django.contrib import admin

from home import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/euro2016'}),
    url(r'^accounts/new/$', 'home.views.register'),

    url(r'^mundial2014/', include('mundial2014.urls')),
    url(r'^euro2016/', include('euro2016.urls')),
)
