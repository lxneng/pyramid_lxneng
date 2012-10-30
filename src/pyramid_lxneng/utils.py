# -*- coding: utf-8 -*-
from webhelpers.paginate import Page
import hashlib
import random
import itertools
from pyramid.security import authenticated_userid
from pyramid.security import has_permission


def get_or_create(session, model, **kw):
    obj = session.query(model).filter_by(**kw).first()
    if obj:
        return obj
    obj = model(**kw)
    session.add(obj)
    return obj


def get_random_word(word_lenght=6):
    chars = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs'
            'tuvwxyz0123456789')
    word = ''
    for i in xrange(word_lenght):
        word += random.choice(chars)
    return word


def generate_hash(url_string):
    m = hashlib.sha256()
    m.update(url_string)
    return m.hexdigest()[:14]


def crop_text(text, length, suffix='...'):
    if not text:
        return text
    if len(text) <= length:
        return text
    return text[:length] + suffix


def grouper(n, iterable, fillvalue=None):
    """grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx

    Copied from http://docs.python.org/library/itertools
    """
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)


def safe_int(value, default):
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


class Tools(object):
    """A collection of tools that can be used in templates."""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def is_anonymous(self):
        return authenticated_userid(self.request) is None

    def has_permission(self, permission):
        """Check if the current user has a certain permission.
        """
        return has_permission(permission, self.context, self.request)

    def paginate(self, items, items_per_page=20):
        """https://bitbucket.org/bbangert/webhelpers/src/acfb17881c1c/webhelpers/paginate.py"""

        current_page = self.request.GET.get('page') or 1

        def page_url(page):
            return self.request.current_route_url(_query={'page': page})

        return Page(collection=items, page=current_page, items_per_page=items_per_page, url=page_url)
