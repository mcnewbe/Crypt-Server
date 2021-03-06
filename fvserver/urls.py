from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import django.contrib.auth.views as auth_views

urlpatterns = [
    # Examples:

    # url(r'^macnamer/', include('macnamer.foo.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^changepassword/$', auth_views.password_change, name='password_change'),
    url(r'^changepassword/done/$', auth_views.password_change_done, name='password_change_done'),
   	url(r'^', include('server.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'namer.views.index', name='home'),

]
