# -*- coding:utf-8 -*-
from enum import unique, IntEnum

from event.event_manager import EventManager
from event.test import event_test


@unique
class Event(IntEnum):
	TEST_EVENT = 1


EVENT_MAP = {
	Event.TEST_EVENT: event_test,
}


EventManager.register_event(EVENT_MAP)
