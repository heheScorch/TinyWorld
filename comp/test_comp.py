# -*- coding: utf-8 -*-
from attr.test_attr import TestAttrEntity
from ecs_core.comp_base import CompBase


class TestComp(CompBase):
	DEPEND_ATTRS = (TestAttrEntity,)

	@classmethod
	def test_func(cls, ent):
		print("test comp test func")
