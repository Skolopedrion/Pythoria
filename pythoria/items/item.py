#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name):
        self.name = name

class Food(Item):
    def __init__(self, name, calories):
        super().__init__(name)
        self.calories = calories


class BaseWeapon(Item):
    def __init__(self, name, dmg_mult):
        super().__init__(name)
        self.dmg_mult = dmg_mult


class ThrowableWeapon(BaseWeapon):
    def __init__(self, name, dmg_mult, range_):
        super().__init__(name, dmg_mult)
        self.range_ = range_


class DistanceWeapon(BaseWeapon):
    def __init__(self, name, dmg_mult, range_, quiver):
        super().__init__(name, dmg_mult)
        self.range_ = range_
        self.quiver = quiver


class BaseMeleeWeapon(BaseWeapon):
    pass


class LightMeleeWeapon(BaseMeleeWeapon):
    hands = 1


class HeavyMeleeWeapon(BaseMeleeWeapon):
    hands = 2