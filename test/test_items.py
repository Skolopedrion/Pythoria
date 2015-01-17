#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from pythoria.items.item import *

class TestItem(unittest.TestCase):
    def test_init(self):
        itm = Item('patate tueuse')
        self.assertEqual(itm.name, 'patate tueuse')

class TestFood(unittest.TestCase):
    def test_init(self):
        fd = Food('bread', calories=40)
        self.assertEqual(fd.name, 'bread')
        self.assertEqual(fd.calories, 40)


class TestBaseWeapon(unittest.TestCase):
    def test_init(self):
        wpn = BaseWeapon('arme', dmg_mult=1.4)
        self.assertEqual(wpn.name, 'arme')
        self.assertAlmostEqual(wpn.dmg_mult, 1.4)

class TestDistanceWeapon(unittest.TestCase):
    def test_init(self):
        wpn = DistanceWeapon('bow', dmg_mult=1.2, range_=9, quiver='bolt')
        self.assertEqual(wpn.name, 'bow')
        self.assertAlmostEqual(wpn.dmg_mult, 1.2)
        self.assertEqual(wpn.range_, 9)
        self.assertEqual(wpn.quiver, 'bolt')


class TestThrowableWeapon(unittest.TestCase):
    def test_init(self):
        wpn = ThrowableWeapon('arme de jet', dmg_mult=1.5, range_=4)
        self.assertEqual(wpn.name, 'arme de jet')
        self.assertAlmostEqual(wpn.dmg_mult, 1.5)


class TestMeleeWeapon(unittest.TestCase):
    def test_init(self):
        wpn = BaseMeleeWeapon('arme de melee', dmg_mult=1.4)
        self.assertEqual(wpn.name, 'arme de melee')
        self.assertAlmostEqual(wpn.dmg_mult, 1.4)


class TestLightMeleeWeapon(unittest.TestCase):
    def test_init(self):
        wpn = LightMeleeWeapon('dague', dmg_mult=1.4)
        self.assertEqual(wpn.name, 'dague')
        self.assertAlmostEqual(wpn.dmg_mult, 1.4)


class TestHeavyMeleeWeapon(unittest.TestCase):
    def test_init(self):
        wpn = HeavyMeleeWeapon('hache lourde', 2.0)
        self.assertEqual(wpn.name, 'hache lourde')
        self.assertAlmostEqual(wpn.dmg_mult, 2.0)


if __name__ == '__main__':
    unittest.main()