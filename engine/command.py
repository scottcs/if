#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if - command """

import log


class _Command(object):
    """ A command """

    def __init__(self, action_token, object_token=None, context=None):
        """ Constructor for _Command """
        self.action_token = action_token
        try:
            self.object_token = object_token.data
            if len(object_token.children) > 0:
                log.error('Don\'t know what to do with children (ignoring): {}'.format(object_token))
        except AttributeError:
            self.object_token = object_token
        self.context = context or {}

    def __repr__(self):
        if self.object_token:
            return '<{}: {} ({}) {} ({})>'.format(self.__class__.__name__,
                                                  self.action_token.type, self.action_token.value,
                                                  self.object_token.type, self.object_token.value)
        else:
            return '<{}: {} ({})>'.format(self.__class__.__name__, self.action_token.type, self.action_token.value)

    def run(self):
        """ Run the command """
        log.debug(self)


class MoveCommand(_Command):
    """ Movement command """


class ExamineCommand(_Command):
    """ Examine command"""


class ManipulateCommand(_Command):
    """ Manipulate command """


_COMMAND_TABLE = {
    'simple_movement': MoveCommand,
    'examine': ExamineCommand,
    'manipulate': ManipulateCommand,
}


def new(cmd_data, context=None):
    """ Make a new command """
    log.debug('Make new command: {}'.format(cmd_data))
    key = cmd_data.data
    try:
        action_token = cmd_data.children[0]
    except (IndexError, TypeError):
        log.error('Couldn\'t get action: {}'.format(cmd_data))
        return None
    try:
        object_token = cmd_data.children[1]
    except (IndexError, TypeError):
        log.debug('No obj found: {}'.format(cmd_data))
        object_token = None
    try:
        cmd = _COMMAND_TABLE[key]
    except KeyError:
        return None
    return cmd(action_token, object_token=object_token, context=context)
