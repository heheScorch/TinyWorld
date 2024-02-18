# -*- coding: utf-8 -*-
from ecs_core.attr_base import AttrEntity, AttrSystem


class TestAttrEntity(AttrEntity):
	def __init__(self):
		super(TestAttrEntity, self).__init__()
		self.a = 0
		self.b = 1


class TestAttrSystem(AttrSystem):
	def __init__(self):
		super(TestAttrSystem, self).__init__()
		self.c = 2
		self.d = 3
