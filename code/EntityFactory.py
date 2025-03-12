#!/usr/bin/python
# -*- coding: utf-8 -*-

from Class4 import Class4
from Class6 import Class6
from Interface1 import Interface1


class EntityFactory(Class4, Class6, Interface1):
    def __init__(self):
        pass

    def get_entity(self, entity_type):
        pass
