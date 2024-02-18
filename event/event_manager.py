# -*- coding: utf-8 -*-


class EventManager(object):
    EVENT_CLS_MAP = {}

    @classmethod
    def register_event(cls, event_map):
        for event_type, event_module in event_map.items():
            cls.EVENT_CLS_MAP[event_type] = event_module.EventDefine

    @classmethod
    def trigger_event(cls, uuid, event_type, arg_dict):
        event_cls = cls.EVENT_CLS_MAP.get(event_type)
        event_cls.trigger(uuid, arg_dict)
