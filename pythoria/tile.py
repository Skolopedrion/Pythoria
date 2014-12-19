# -*- coding: utf-8 -*-

class Tile(object):
    """
    The tile contains all the information regarding its visibility, if
    it blocks line of sight, ...
    """

    def __init__(self, value=' ', block_light=False, blocking=False, visible=False):
        self.value = value
        self.block_light = block_light
        self.blocking = blocking
        self.visible = visible

    def __eq__(self, other):
        return self.value == other.value and \
               self.block_light == other.block_light and \
               self.blocking == other.blocking and \
               self.visible == other.visible

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return '<Tile {0}{1}>'.format(self.value, ' visible' if self.visible else '')

    def __str__(self):
        return self.value