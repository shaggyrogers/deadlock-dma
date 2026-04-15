#!/usr/bin/env python3
"""
HeroID.py
=========

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-12
Modification Date:     2026-04-12

"""

from enum import IntEnum

_HERO_ID_NAMES = {
    1: "Infernus",
    2: "Seven",
    3: "Vindicta",
    4: "LadyGeist",
    6: "Abrams",
    7: "Wraith",
    8: "McGinnis",
    10: "Paradox",
    11: "Dynamo",
    12: "Kelvin",
    13: "Haze",
    14: "Holliday",
    15: "Bebop",
    16: "Calico",
    17: "GreyTalon",
    18: "MoAndKrill",
    19: "Shiv",
    20: "Ivy",
    25: "Warden",
    27: "Yamato",
    31: "Lash",
    35: "Viscous",
    48: "Wrecker",
    50: "Pocket",
    52: "Mirage",
    55: "Dummy",
    58: "Vyper",
    60: "Sinclair",
    63: "Mina",
    64: "Drifter",
    65: "Venator",
    66: "Victor",
    67: "Paige",
    69: "Doorman",
    72: "Billy",
    76: "Graves",
    77: "Apollo",
    79: "Rem",
    80: "Silver",
    81: "Celeste",
}

HeroID = IntEnum("HeroID", ((v, k) for k, v in _HERO_ID_NAMES.items()))
