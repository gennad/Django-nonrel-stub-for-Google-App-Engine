from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'views.index'),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
