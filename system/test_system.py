# -*- coding: utf-8 -*-
from attr.test_attr import TestAttrEntity, TestAttrSystem
from comp.test_comp import TestComp
from ecs_core.system_base import SystemBase
from ecs_core.system_manager import system_register
from event.event_const import Event
from event.event_manager import EventManager


@system_register
class TestSystem(SystemBase):
	PROCESS_COMPS = (TestComp,)
	ATTRS = (TestAttrSystem,)

	def __init__(self):
		super(TestSystem, self).__init__()

	def init(self, init_dict):
		super(TestSystem, self).init(init_dict)

	def tick(self):
		super(TestSystem, self).tick()
		self.test_func()

	def test_func(self):
		for ent in self._entities:
			EventManager.trigger_event(ent.uuid, Event.TEST_EVENT, {})
