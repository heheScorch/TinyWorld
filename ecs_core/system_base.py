# -*- coding: utf-8 -*-
from helper.decorators import singleton
from log.log_manager import LogManager


@singleton
class SystemBase(object):
	PROCESS_COMPS = ()
	ATTRS = ()
	ACTIVE = True

	def __init__(self):
		self._entities = set()
		self._attrs = {}
		self._logger = None

	def init(self, init_dict):
		self.init_attrs()

	def init_attrs(self):
		for attr in self.ATTRS:
			attr_ins = attr()
			self._attrs[attr] = attr_ins

	def init_logger(self):
		self._logger = LogManager.get_debug_logger(self.__class__.__name__)

	def __getitem__(self, item):
		if item in self.ATTRS:
			return self._attrs[item]

	def register_entity(self, ent):
		self._entities.add(ent)

	@property
	def entities(self):
		return self._entities

	def tick(self):
		pass
