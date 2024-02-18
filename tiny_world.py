# -*- coding: utf-8 -*-
import time
import traceback

import config
from ecs_core import system_manager
from entity.individual_entity import IndividualEntity
from entity.test_entity import TestEntity
from helper.decorators import singleton

import entity       # noqa
import comp         # noqa
import system       # noqa
from log.log_manager import LogManager


@singleton
class TinyWorld(object):

	def __init__(self):
		self._systems = system_manager.get_all_system()
		self._entities = {}
		self._logger = LogManager.get_world_logger()

	def generate_init_entities(self):
		ent = IndividualEntity()
		ent.init()

	def run(self):
		self._logger.info("hello, tiny world")
		for s in self._systems:
			s.init()
		self.generate_init_entities()
		self.main_loop()

	def main_loop(self):
		last_execution_time = 0
		while(True):
			current_time = time.time()
			if current_time - last_execution_time >= config.SYSTEM_TICK_INTERVAL:
				self.tick()
				last_execution_time = time.time()
			time.sleep(0.01)

	def tick(self):
		for s in self._systems:
			if s.ACTIVE:
				s.tick()

	def stop(self):
		pass

# todo: 事件系统
