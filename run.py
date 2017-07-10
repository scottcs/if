#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" if - run """

from __future__ import print_function
import argparse

import engine
import engine.game


def get_args():
    """ Get command line arguments
    :return: args as a dict
    """
    arg_parser = argparse.ArgumentParser(description='run the if')
    arg_parser.add_argument('story', help='story to run')
    arg_parser.add_argument('-D', '--debug',
                            action='store_true',
                            help='turn on debugging')

    args = arg_parser.parse_args()
    return vars(args)


def main():
    """ Main function """
    args = get_args()
    print('ARGS: {}'.format(args))
    game = engine.game.Game(args['story'], args['debug'])
    game.run()


if __name__ == '__main__':
    main()
