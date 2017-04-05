from django.conf.urls import include, url
from django.contrib import admin
from formulaireEsig import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'esigapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^uti_list', views.uti_list, name='uti_list'),
]
