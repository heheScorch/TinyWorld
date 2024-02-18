# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from attr.system_attr import TimeSystemAttr
from comp.time_comp import TimeComp
from ecs_core.system_base import SystemBase
from ecs_core.system_manager import system_register


class WorldTime(object):
	second = 0
	minute = 0
	hour = 0
	day = 0
	month = 0
	year = 0


@system_register
class TimeSystem(SystemBase):
	PROCESS_COMPS = (TimeComp,)
	ATTRS = (TimeSystemAttr,)

	def __init__(self):
		super(TimeSystem, self).__init__()

	def init(self, init_dict):
		super(TimeSystem, self).init(init_dict)
		self.init_current_time()

	def init_current_time(self, world_time=None):
		current_time = world_time if world_time else datetime.now()
		self[TimeSystemAttr].second = current_time.second
		self[TimeSystemAttr].minute = current_time.minute
		self[TimeSystemAttr].hour = current_time.hour
		self[TimeSystemAttr].day = current_time.day
		self[TimeSystemAttr].month = current_time.month
		self[TimeSystemAttr].year = current_time.year

	def tick(self):
		super(TimeSystem, self).tick()
		self.time_elapse(seconds=1)
		print(TimeComp.get_current_time())

	def time_elapse(self, seconds):
		current_time = TimeComp.get_current_time()
		elapsed_time = current_time + timedelta(seconds=seconds)
		self.init_current_time(elapsed_time)

	def get_day_of_the_week(self):
		date = "%s-%s-%s" % (self[TimeSystemAttr].year, self[TimeSystemAttr].month, self[TimeSystemAttr].day)
		date_obj = datetime.strptime(date, '%Y-%m-%d')
		weekday = date_obj.weekday()
		return weekday + 1
