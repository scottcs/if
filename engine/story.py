#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if engine - Story """

import os


_UNKNOWN = 'UNKNOWN'


def _load_grammar(grammar_name):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'grammars')
    filename = '{}.g'.format(grammar_name)
    with open(os.path.join(path, filename)) as f:
        text = f.read()
    return text


class Story(object):
    """ Story class """

    def __init__(self, loaded_module):
        """ Constructor for Story """
        self._meta = loaded_module.META
        self._grammar = _load_grammar(self.grammar_name)
        self._rooms = loaded_module.ROOMS
        self._items = loaded_module.ITEMS

    @property
    def name(self):
        """ name property getter """
        return self._meta.get('name', _UNKNOWN)

    @property
    def author(self):
        """ author property getter """
        return self._meta.get('author', _UNKNOWN)

    @property
    def created_on(self):
        """ created_on property getter """
        return self._meta.get('created', _UNKNOWN)

    @property
    def grammar_name(self):
        """ grammar_name property getter """
        return self._meta.get('grammar', _UNKNOWN)

    @property
    def grammar(self):
        """ grammar property getter """
        return self._grammar

    @property
    def rooms(self):
        """ rooms property getter """
        return self._rooms

    @property
    def items(self):
        """ items property getter """
        return self._items
