# -*- coding: utf-8 -*-


class EntityManager(object):
	ENTITY_MAP = {}

	@classmethod
	def add_entity(cls, ent):
		cls.ENTITY_MAP[ent.uuid] = ent

	@classmethod
	def remove_entity(cls, uuid):
		cls.ENTITY_MAP.pop(uuid, None)

	@classmethod
	def get_entity(cls, uuid):
		return cls.ENTITY_MAP.get(uuid)
