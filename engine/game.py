#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if engine - game """

from __future__ import print_function
import sys

import lark

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

    def __init__(self, story_name):
        self._story = _load_story(story_name)
        self._parser = lark.Lark(self._story.grammar)

    def run(self):
        """ Run the game """
        print('RUN {}'.format(self._story.name))
        while True:
            command = raw_input('> ')
            # noinspection PyBroadException
            try:
                self._parse_command(command)
            except Exception as exc:
                if isinstance(exc, KeyboardInterrupt):
                    print('Quitting...')
                    break
                print(sys.exc_info()[0])

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
        print(command)
        print(dir(command))
        print(command.data)
        print(dir(command.data))
        print(command.children)
        print(dir(command.children))
        for sub in command.iter_subtrees():
            print(sub)
            print(sub.__class__)
            print(sub.data)
            for child in sub.children:
                print(child)
                print(child.__class__)
                print(child.type, child.value)
