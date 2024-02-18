# -*- coding: utf-8 -*-
from attr.system_attr import TimeSystemAttr
from comp.time_comp import TimeComp
from ecs_core.system_base import SystemBase
from ecs_core.system_manager import system_register


@system_register
class TimeSystem(SystemBase):
	PROCESS_COMPS = (TimeComp,)
	ATTRS = (TimeSystemAttr,)

	def __init__(self):
		super(TimeSystem, self).__init__()

	def init(self):
		super(TimeSystem, self).init()

	def tick(self):
		super(TimeSystem, self).tick()
		for ent in self.entities:
			print(ent[TimeComp].get_current_time(ent))
