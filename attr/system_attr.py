# -*- coding: utf-8 -*-
from ecs_core.attr_base import AttrSystem


class TimeSystemAttr(AttrSystem):
    def __init__(self):
        super(TimeSystemAttr, self).__init__()
        self.year = None
        self.month = None
        self.day = None
        self.hour = None
        self.minute = None
        self.second = None
