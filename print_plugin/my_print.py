# -*- coding: utf-8 -*-
from pokemongo_bot.base_task import BaseTask


class Print(BaseTask):
    SUPPORTED_TASK_API_VERSION = 1

    def work(self):
        print 'PrintPlugin!'
