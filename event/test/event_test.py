# -*- coding: utf-8 -*-
from comp.test_comp import TestComp
from ecs_core.entity_manager import EntityManager
from event.event_base import EventBase
from log.log_manager import LogManager

_logger = LogManager.get_debug_logger('event_test')


class EventDefine(EventBase):
	@classmethod
	def _trigger(cls, uuid, arg_dict):
		ent = EntityManager.get_entity(uuid)
		if not ent:
			_logger.warning("trigger event non exist ent, uuid: %s" % uuid)
			return
		ent[TestComp].test_func()
