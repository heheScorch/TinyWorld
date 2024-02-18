# -*- coding: utf-8 -*-
from ecs_core.comp_base import CompBase


class AIBTComp(CompBase):
    DEPEND_ATTRS = ()

    @classmethod
    def start(cls):
        pass

    def stop(self):
        pass

    def resume(self):
        pass

    def pause(self):
        pass
