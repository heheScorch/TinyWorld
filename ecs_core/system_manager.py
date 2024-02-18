# -*- coding: utf-8 -*-

_ALL_SYSTEM = {}


def system_register(cls):
	_ALL_SYSTEM[cls.__name__] = cls
	return cls


def get_all_system():
	return [s() for s in _ALL_SYSTEM.values()]


def get_system_instance(system_name):
	sys = _ALL_SYSTEM.get(system_name)
	if sys:
		return sys()
