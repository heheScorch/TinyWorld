# -*- coding: utf-8 -*-
from enum import Enum

SYSTEM_TICK_INTERVAL = 1


class LoggerType(Enum):
    ENTITY_LOGGER = 1
    COMP_LOGGER = 2
    SYSTEM_LOGGER = 3
