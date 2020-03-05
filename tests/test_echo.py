#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_uppper(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "hello"],
            stdout=subprocess.PIPE)
        args_u = process.args
        stdout, _ = process.communicate()
        stdout_u = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--upper", "hello"],
            stdout=subprocess.PIPE)
        args_upper = process.args
        stdout, _ = process.communicate()
        stdout_upper = stdout.decode("utf-8")

        usage = open("./USAGEUPPER", "r").read()
        self.assertEquals(stdout_u, usage)
        self.assertEqual("-u" in args_u, True)
        self.assertEquals(stdout_upper, usage)
        self.assertEqual("--upper" in args_upper, True)

    def test_lower(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "Hello"],
            stdout=subprocess.PIPE)
        args_l = process.args
        stdout, _ = process.communicate()
        stdout_l = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--lower", "Hello"],
            stdout=subprocess.PIPE)
        args_lower = process.args
        stdout, _ = process.communicate()
        stdout_lower = stdout.decode("utf-8")

        usage = open("./USAGELOWER", "r").read()
        self.assertEquals(stdout_l, usage)
        self.assertEqual("-l" in args_l, True)
        self.assertEquals(stdout_lower, usage)
        self.assertEqual("--lower" in args_lower, True)

    def test_title(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello"],
            stdout=subprocess.PIPE)
        args_t = process.args
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--title", "hello"],
            stdout=subprocess.PIPE)
        args_title = process.args
        stdout, _ = process.communicate()
        stdout_title = stdout.decode("utf-8")

        usage = open("./USAGETITLE", "r").read()
        self.assertEquals(stdout_t, usage)
        self.assertEqual("-t" in args_t, True)
        self.assertEquals(stdout_title, usage)
        self.assertEqual("--title" in args_title, True)

    def test_select_all(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "-u", "-l", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")
        usage_t = open("./USAGETITLE", "r").read()
        self.assertEquals(stdout_t, usage_t)

        process = subprocess.Popen(
            ["python", "./echo.py", "--title", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")
        usage_t = open("./USAGETITLE", "r").read()
        self.assertEquals(stdout_t, usage_t)

        process = subprocess.Popen(
            ["python", "./echo.py", "--title", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")
        usage_t = open("./USAGETITLE", "r").read()
        self.assertEquals(stdout_t, usage_t)

    def test_no_arguments(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "hElLo"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")
        usage = open("./USAGENONE", "r").read()
        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
