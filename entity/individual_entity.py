# -*- coding: utf-8 -*-
from comp.test_comp import TestComp
from comp.time_comp import TimeComp
from ecs_core.entity_base import EntityBase


class IndividualEntity(EntityBase):
	COMPS = (TimeComp, TestComp,)
	ATTRS = ()
