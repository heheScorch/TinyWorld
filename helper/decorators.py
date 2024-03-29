# -*- coding: utf-8 -*-

import functools


def singleton(cls):
	# 支持热更的单例实现，cls()返回实例

	cls.__new_original__ = cls.__new__

	@functools.wraps(cls.__new__)
	def singleton_new(cls, *args, **kw):
		it = cls.__dict__.get('__it__')
		if it is not None:
			return it

		cls.__it__ = it = cls.__new_original__(cls, *args, **kw)
		it.__init_original__(*args, **kw)
		return it

	cls.__new__ = staticmethod(singleton_new)
	cls.__init_original__ = cls.__init__
	cls.__init__ = object.__init__

	return cls
