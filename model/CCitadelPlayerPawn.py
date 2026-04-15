#!/usr/bin/env python3
"""
CCitadelPlayerPawn.py
=====================

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-08
Modification Date:     2026-04-15

"""

import struct


class CCitadelPlayerPawn:
    """ """

    SIZE = 0x2000

    def __init__(self, data: bytes) -> None:
        """Initialises a CCitadelPlayerPawn instance."""
        self.gameSceneNode = None
        self.m_pGameSceneNode = int.from_bytes(
            data[0x330:0x338], byteorder="little"
        )  # CGameSceneNode*

        self.m_iMaxHealth = int.from_bytes(data[0x350:0x354], byteorder="little")
        self.m_iHealth = int.from_bytes(data[0x354:0x358], byteorder="little")
        self.m_lifeState = data[0x35C]

        self.m_flSpeed = struct.unpack("f", data[0x3EC:0x3F0])[0]

        self.m_iTeamNum = data[0x3F3]

        self.vecAbsVelocity = struct.unpack("3f", data[0x404:0x410])  # Vector
        self.v_angle = struct.unpack("3f", data[0xF98:0xFA4])  # QAngle
