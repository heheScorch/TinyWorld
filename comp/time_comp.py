# -*- coding: utf-8 -*-
from attr.system_attr import TimeSystemAttr
from ecs_core import system_manager
from ecs_core.comp_base import CompBase


class TimeComp(CompBase):
	DEPEND_ATTRS = ()

	@classmethod
	def get_current_time(cls, ent):
		time_system = system_manager.get_system_instance("TimeSystem")
		return time_system[TimeSystemAttr]
