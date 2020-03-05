#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "troyerjl and knmarvel code as a resource"


import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Take a command line input and perform it on an input text")
    parser.add_argument("text",
                        help="text to be manipulated")
    parser.add_argument("-u",
                        "--upper",
                        action="store_const",
                        const=bool,
                        help="Upper case conversion command")
    parser.add_argument("-l",
                        "--lower",
                        action="store_const",
                        const=bool,
                        help="Lower case conversion command")
    parser.add_argument("-t",
                        "--title",
                        action="store_const",
                        const=bool,
                        help="Title case conversion command")
    return parser.pars_args()


def main(args):
    """Implementation of echo"""
    args = create_parser()
    text = args.text

    if text.upper:
        text = text.upper()
    if text.lower:
        text = text.lower()
    if text.title:
        text = text.title()

    print(text)


if __name__ == '__main__':
    pass
