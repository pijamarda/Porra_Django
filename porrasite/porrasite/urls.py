from django.conf.urls import patterns, include, url

from django.contrib import admin

from mundial2014 import views




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'porrasite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/mundial'}),
    url(r'^accounts/new/$', 'mundial2014.views.register'),

    url(r'^mundial/', include('mundial2014.urls')),
)
