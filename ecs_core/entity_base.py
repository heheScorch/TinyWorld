# -*- coding: utf-8 -*-
import uuid

from ecs_core import system_manager
from helper.container_helper import is_list_intersect


class EntityBase(object):

	COMPS = ()
	ATTRS = ()

	def __init__(self):
		self._attrs = {}
		self._uuid = uuid.uuid4()

	def init(self):
		self.init_attrs()
		self.register_to_system()

	def init_attrs(self):
		for attr in self.ATTRS:
			attr_ins = attr()
			self._attrs[attr] = attr_ins

	def register_to_system(self):
		""" 向各个系统注册 """
		for s in system_manager.get_all_system():
			if is_list_intersect(s.PROCESS_COMPS, self.COMPS):
				s.register_entity(self)

	def __getitem__(self, item):
		if item in self.COMPS:
			return item
		elif item in self.ATTRS:
			return self._attrs[item]

	@property
	def uuid(self):
		return self._uuid
