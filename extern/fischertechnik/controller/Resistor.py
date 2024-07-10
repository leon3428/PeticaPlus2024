#!/usr/bin/python
# -*- coding: UTF-8 -*-
from .Input import Input

class Resistor(Input):
    def __init__(self, controller, identifier):
        """@ParamType controller fischertechnik.controller.BaseController
        @ParamType identifier int"""
        Input.__init__(self, controller, identifier)

    def get_resistance(self):
        """@ReturnType int"""
        pass
