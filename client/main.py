#!/usr/bin/env python
# encoding: utf-8
# 2014-10-13 16:43:57.124696

# Get a logger
from utils.log import logger
# Get an options parser
from utils.opts import OptionsParser
from session import Session


class MySession(Session):
    def run(self):
        print("My Run!!!")
        self.vim.command('echo "some shit %s"' % __name__)


def main():
    op = OptionsParser()
    session = MySession()
    session.start()


if __name__ == '__main__':
    main()
