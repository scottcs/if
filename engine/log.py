#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if - log """

import logging


def make_log(name, debug=False):
    """ Make a new logging object

    :param name: name of log
    :param debug: if True, set level to DEBUG
    :return: logging object
    """
    log = logging.getLogger(name)
    if not log.handlers:
        log.propagate = False
        log.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s]=%(levelname)s=> %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        log.addHandler(stream_handler)
    if debug:
        log.setLevel(logging.DEBUG)
    return log
