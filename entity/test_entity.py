# -*- coding: utf-8 -*-
from attr.test_attr import TestAttrEntity
from comp.test_comp import TestComp
from ecs_core.entity_base import EntityBase


class TestEntity(EntityBase):
	COMPS = (TestComp,)
	ATTRS = (TestAttrEntity,)

