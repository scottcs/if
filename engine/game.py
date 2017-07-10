#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if engine - game """

from __future__ import print_function
import sys

import lark

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
        self.log = log.make_log(story_name, debug=debug)

    def run(self):
        """ Run the game """
        self.log.info('RUN {}'.format(self._story.name))
        while True:
            command = raw_input('> ')
            # noinspection PyBroadException
            try:
                self._parse_command(command)
            except Exception as exc:
                if isinstance(exc, KeyboardInterrupt):
                    self.log.info('Quitting...')
                    break
                self.log.exception(sys.exc_info()[0])

    def _parse_command(self, command):
        """ Parse a command

        :param command: raw input command string
        """
        parse_tree = self._parser.parse(command)
        print(parse_tree.pretty())
        for instruction in parse_tree.children:
            self._run_command(instruction)

    def _run_command(self, command):
        """ Run a command

        :param command: parsed command
        """
        for sub in command.iter_subtrees():
            if sub.data == 'examine':
                self._examine(*sub.children)
            else:
                self.log.error(sub.children)

    def _examine(self, verb, obj):
        """ Examine an object

        :param verb: the examine verb token
        :param obj: the examine object token
        """
        self.log.debug('verb: {} ({})   obj: {} ({})'.format(verb, verb.type, obj, obj.type))
        if verb.type == 'EXAMINE' and obj.type == 'OBJECT':
            self.log.debug('// PRINT DESCRIPTION OF OBJECT')
            self._describe(obj.value)
        else:
            self.log.error('Unknown grammar: {} {}'.format(verb.type, obj.type))

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
