from django.conf.urls import patterns, include, url


# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'o2bra_cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^admin/', include(admin.site.urls)),
    
    (r'^list$', 'o2bra_cms.collections.views.list'),
    (r'^add$', 'o2bra_cms.collections.views.add'),
    (r'^index$', 'o2bra_cms.collections.views.index'),
)
