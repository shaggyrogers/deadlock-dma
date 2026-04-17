#!/usr/bin/env python3
"""
CGameSceneNode.py
=================

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-12
Modification Date:     2026-04-17

"""

from construct import Struct, Array, Float32l, Padding

CGameSceneNode = Struct(
    Padding(0xB8),
    "m_angRotation" / Array(3, Float32l),  # QAngle
    "m_flScale" / Float32l,
    "m_vecAbsOrigin" / Array(3, Float32l),  # VectorWS
    "m_angAbsRotation" / Array(3, Float32l),  # QAngle
    Padding(0x48),
    "m_vRenderOrigin" / Array(3, Float32l),  # Vector
)
