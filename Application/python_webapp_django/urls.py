"""
Definition of urls for python_webapp_django.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import include, path
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^show_orders', app.views.show_orders, name='show_orders'),
    url(r'^manage_order', app.views.manage_order, name='manage_order'),
    url(r'^create_order', app.views.create_order, name='create_order'),
    url(r'^add_profile_info', app.views.add_profile_info, name='add_profile_info'),
    path('cancel_order/<int:order_id>/', app.views.cancel_order, name='cancel_order'),
    url(r'^login/$',
        django.contrib.auth.views.LoginView,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout/$',
        django.contrib.auth.views.LogoutView,
        {
            'next_page': '/'
        },
        name='logout'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
]
