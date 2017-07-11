#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if - log """

import logging


_log = None


def init(name, debugging=False):
    """ Make a new logging object

    :param name: name of log
    :param debugging: if True, set level to DEBUG
    :return: logging object
    """
    global _log
    _log = logging.getLogger(name)
    if not _log.handlers:
        _log.propagate = False
        _log.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s]=%(levelname)s=> %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        _log.addHandler(stream_handler)
    if debugging:
        _log.setLevel(logging.DEBUG)


# noinspection PyMissingOrEmptyDocstring
def debug(*args, **kwargs):
    global _log
    if _log:
        return _log.debug(*args, **kwargs)


# noinspection PyMissingOrEmptyDocstring
def info(*args, **kwargs):
    global _log
    if _log:
        return _log.info(*args, **kwargs)


# noinspection PyMissingOrEmptyDocstring
def warn(*args, **kwargs):
    global _log
    if _log:
        return _log.warn(*args, **kwargs)


# noinspection PyMissingOrEmptyDocstring
def error(*args, **kwargs):
    global _log
    if _log:
        return _log.debug(*args, **kwargs)


# noinspection PyMissingOrEmptyDocstring
def exception(*args, **kwargs):
    global _log
    if _log:
        return _log.exception(*args, **kwargs)


# noinspection PyMissingOrEmptyDocstring
def critical(*args, **kwargs):
    global _log
    if _log:
        return _log.critical(*args, **kwargs)
