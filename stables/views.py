u"""
🐴
✔
✘
▏
"""
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from urllib.parse import quote
from . import models


def badge_escape(val):
    return quote(val.replace('-', '--'))


class BadgeView(RedirectView):

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        filter_arg = Q(
            package__name=kwargs['package_name'],
        )
        try:
            filter_arg &= Q(
                version=kwargs['package_version'],
            )
        except KeyError:
            pass
        try:
            filter_arg &= Q(
                result__installed_packages__contains={
                    kwargs['factor_name']: kwargs['factor_version'],
                },
            )
        except KeyError:
            try:
                filter_arg &= Q
                    result__installed_packages__has_key=kwargs['factor_name'],
                )

        status = get_object_or_404(models.PackageVersion, filter_arg)
        for result in status.result_set.objects.filter(
        color = {
            'passed': 'green',
        }[kwargs['result']
        return quote(
            u'https://img.shields.io/badge/ 🐴  Supports %s - %s -%s.svg' % (
                badge_escape(kwargs['package_name']),
                badge_escape(kwargs['factor_name']),
                color,
            ),
        )
