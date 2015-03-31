from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.formset_nested.views import CreateContactView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'formsets_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/news', CreateContactView.as_view(), name='example1'),


)
