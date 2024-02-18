# -*- coding: utf-8 -*-
from log.log_manager import LogManager

_logger = LogManager.get_debug_logger('EventBase')


class EventBase(object):
	@classmethod
	def trigger(cls, uuid, arg_dict):
		cls._trigger(uuid, arg_dict)

	@classmethod
	def _trigger(cls, uuid, arg_dict):
		raise NotImplementedError('%s has not implement _do func.' % (cls.__name__,))
