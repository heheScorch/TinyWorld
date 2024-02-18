# -*- coding: utf-8 -*-
from datetime import datetime

from attr.system_attr import TimeSystemAttr
from ecs_core import system_manager
from ecs_core.comp_base import CompBase


class TimeComp(CompBase):
	DEPEND_ATTRS = ()

	@classmethod
	def get_current_time(cls):
		time_system = system_manager.get_system_instance("TimeSystem")
		return cls.format_time(time_system[TimeSystemAttr])

	@classmethod
	def format_time(cls, attr):
		time_str = "%s-%s-%s %s:%s:%s" % (attr.year, attr.month, attr.day, attr.hour, attr.minute, attr.second)
		date_format = "%Y-%m-%d %H:%M:%S"
		return datetime.strptime(time_str, date_format)
