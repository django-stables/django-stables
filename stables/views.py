u"""
🐴
✔
✘
▏
"""
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from urllib.parse import quote
from . import models


class BadgeView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        status = get_object_or_404(
            models.PackageVersion,
            package__name=kwargs['package_name'],
            version=kwargs['package_version'],
            **{
                'result__installed_packages__%(factor_name)s' % kwargs:
                    kwargs['factor_version'],
            }
        )
        return quote(
            'https://img.shields.io/badge/ 🐴  {} - {} -{}.svg'.format(
                *args
            ),
        )
