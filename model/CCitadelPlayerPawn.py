#!/usr/bin/env python3
"""
CCitadelPlayerPawn.py
=====================

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-08
Modification Date:     2026-04-17

"""

from construct import Struct, Array, Int8ul, Int32ul, Int64ul, Float32l, Padding

CCitadelPlayerPawn = Struct(
    Padding(0x330),
    "m_pGameSceneNode" / Int64ul,
    Padding(0x18),
    "m_iMaxHealth" / Int32ul,
    "m_iHealth" / Int32ul,
    Padding(0x4),
    "m_lifeState" / Int8ul,
    Padding(0x8F),
    "m_flSpeed" / Float32l,
    Padding(0x3),
    "m_iTeamNum" / Int8ul,
    Padding(0x10),
    "vecAbsVelocity" / Array(3, Float32l),
    Padding(0xB88),
    "v_angle" / Array(3, Float32l),  # QAngle
)
