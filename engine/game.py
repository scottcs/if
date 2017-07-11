#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if engine - game """

from __future__ import print_function
import sys

import lark

import command
import log
import story


def _load_story(story_name):
    """ Load a story module

    :param story_name: name of the story module
    :return: a Story object
    """
    module_name = 'stories.{}'.format(story_name)
    __import__(module_name)
    print('Story "{}" Loaded...'.format(story_name))
    return story.Story(sys.modules[module_name])


class Game(object):
    """ Game Class"""

    def __init__(self, story_name, debug=False):
        self._story = _load_story(story_name)
        self._parser = lark.Lark(self._story.grammar)
        log.init(story_name, debugging=debug)

    def run(self):
        """ Run the game """
        log.info('RUN {}'.format(self._story.name))
        while True:
            cmd = raw_input('> ')
            # noinspection PyBroadException
            try:
                self._parse_command(cmd)
            except Exception as exc:
                if isinstance(exc, KeyboardInterrupt):
                    log.info('Quitting...')
                    break
                log.exception(sys.exc_info()[0])

    def _parse_command(self, cmd):
        """ Parse a command

        :param cmd: raw input command string
        """
        try:
            parse_tree = self._parser.parse(cmd)
        except lark.ParseError:
            print('I don\'t understand that command.')
            return
        log.debug('\n{}'.format(parse_tree.pretty()))
        for instruction in parse_tree.children:
            self._run_command(instruction)

    def _run_command(self, cmd):
        """ Run a command

        :param cmd: parsed command
        """
        cmd_obj = command.new(cmd.children[0])
        if cmd_obj:
            cmd_obj.run()

    def _examine(self, verb, obj):
        """ Examine an object

        :param verb: the examine verb token
        :param obj: the examine object token
        """
        log.debug('verb: {} ({})   obj: {} ({})'.format(verb, verb.type, obj, obj.type))
        if verb.type == 'EXAMINE' and obj.type == 'OBJECT':
            log.debug('// PRINT DESCRIPTION OF OBJECT')
            self._describe(obj.value)
        else:
            log.error('Unknown grammar: {} {}'.format(verb.type, obj.type))

    def _describe(self, obj):
        """ Describe an item or room

        :param obj: the item or room to describe
        """
        try:
            print(self._story.items[obj]['description'])
        except KeyError:
            try:
                print(self._story.rooms[obj]['description'])
            except KeyError:
                print('I don\'t see {}.'.format(obj))
