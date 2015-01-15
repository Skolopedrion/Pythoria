#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name):
        self.name = name

class Food(Item):
    def __init__(self, name, calories):
        super().__init__(name)
        self.calories = calories


class Weapon:
    def __init__(self, name, dmg_mult):
        self.name = name
        self.dmg_mult = dmg_mult


class ThrowableWeapon(Weapon):
    def __init__(self, name, dmg_mult, range):
        super().__init__(name, dmg_mult)
        self.range = range


class DistanceWeapon(Weapon):
    def __init__(self, name, dmg_mult, range, quiver):
        super().__init__(name, dmg_mult)
        self.range = range
        self.quiver = quiver


class MeleeWeapon(Weapon):
    pass


class LightMeleeWeapon(MeleeWeapon):
    hands = 1


class HeavyMeleeWeapon(MeleeWeapon):
    hands = 2