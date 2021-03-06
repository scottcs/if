#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if - command """

from . import log


class _Command(object):
    """ A command """

    def __init__(self, action_token, object_token=None, third_token=None, context=None):
        """ Constructor for _Command """
        self.action_token = action_token
        self.object_token = object_token
        self.third_token = third_token
        self.context = context or {}

    def __repr__(self):
        string = '<{}: {} ({})'.format(self.__class__.__name__, self.action_token.type, self.action_token.value)
        if self.object_token:
            string += ' {} ({})'.format(self.object_token.type, self.object_token.value)
        if self.third_token:
            string += ' {} ({})'.format(self.third_token.type, self.third_token.value)
        string += '>'
        return string

    def _usage(self):
        """ Return usage string list """
        return ['Usage: command']

    def _description(self):
        """ Return description string list """
        return ['I don\'t really know either.']

    def run(self):
        """ Run the command """
        log.debug(self)


class MoveCommand(_Command):
    """ Movement command """


class ExamineCommand(_Command):
    """ Examine command"""


class ManipulateCommand(_Command):
    """ Manipulate command """


class OptionCommand(_Command):
    """ Option command """


class HelpCommand(_Command):
    """ Help command """

    def run(self):
        super(HelpCommand, self).run()
        print('Usage:')

    def _description(self):
        return [
            'Get help on a command.',
            'Supported Commands:',
            '  help, option, look, north, south, east, west, up, down, open, close',  # TODO: automate this
        ]

    def _usage(self):
        return [
            'help, ? - this help',
            'help TOPIC, ? TOPIC - get help on TOPIC',
        ]


_COMMAND_TABLE = {
    'simple_movement': MoveCommand,
    'examine': ExamineCommand,
    'manipulate': ManipulateCommand,
    'option': OptionCommand,
    'help': HelpCommand,
}


def new(cmd_data, context=None):
    """ Make a new command """
    log.debug('Make new command: {}'.format(cmd_data))
    key = cmd_data.data
    try:
        action_token = cmd_data.children[0]
    except (IndexError, TypeError):
        log.error('Couldn\'t get action token: {}'.format(cmd_data))
        return None
    try:
        object_token = cmd_data.children[1]
    except (IndexError, TypeError):
        log.debug('No object token found: {}'.format(cmd_data))
        object_token = None
    try:
        third_token = cmd_data.children[2]
    except (IndexError, TypeError):
        log.debug('No third token found: {}'.format(cmd_data))
        third_token = None
    try:
        cmd = _COMMAND_TABLE[key]
    except KeyError:
        return None
    return cmd(action_token, object_token=object_token, third_token=third_token, context=context)
