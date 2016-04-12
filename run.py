#!/usr/bin/env python
import sys

from src.bot import Bot

import logging

from src.botfactory import BotFactory


def main():

    logging.basicConfig(level=logging.INFO)

    bot = BotFactory().create('taunts')


    bot.run("MTY4Nzg2OTI5MDI5MDg3MjMz.Cewqkw.aPrQqRYJollVn_vP606qvbV-5ww")

if __name__ == '__main__':
    main()
