# coding=utf-8
import os

__author__ = 'Vasu Babu Kandimalla <lana.pcfre@gmail.com>'


def update_settings(settings):
    """Update settings file for fluentgrid."""
    settings.INSTALLED_APPS += ("fluentgrid", )
    settings.INSTALLED_APPS = list(settings.INSTALLED_APPS)

    # Make priority for geosafe templates
    template_dirs = list(settings.TEMPLATES[0]['DIRS'])
    template_dirs.insert(0, '/usr/src/fluentgrid/templates')

    settings.TEMPLATES[0]['DIRS'] = template_dirs
    settings.STATICFILES_DIRS += (
        '/usr/src/fluentgrid/static',
    )
