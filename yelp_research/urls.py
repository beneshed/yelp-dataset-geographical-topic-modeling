from django.conf.urls import patterns, include, url
from django.http import HttpResponse
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mining import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yelp_research.views.home', name='home'),
    # url(r'^yelp_research/', include('yelp_research.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
    #Mining App
     url(r'^mining/', include('mining.urls')),

    #Main Page is Login
     url(r'^$', views.index, name='index'),

    #robots
     url(r'^robots.txt', lambda r: HttpResponse("User-agent: Googlebot \nDisallow: \nUser-agent: *\nDisallow: /", mimetype="text/plain")),

     url(r'^about', views.about, name='about'),

     url(r'^research_paper', views.research_paper, name='research_paper'),

     url(r'^reviews', views.reviews, name='reviews'),

     url(r'^restaurants', views.restaurants, name='restaurants'),

     url(r'^legal', views.legal, name='legal'),

     url(r'^map', views.research_map, name='map'),

     url(r'^contact_me', views.contact_me, name='contact_me'),

    #Portal
    # url(r'^portal/', include('portal.urls')),
     
)
