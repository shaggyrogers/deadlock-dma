#!/usr/bin/env python3
"""
CCitadelPlayerController.py
===========================

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-08
Modification Date:     2026-04-17

"""

from .PlayerDataGlobal import PlayerDataGlobal

from construct import Struct, Int8ul, Int32ul, Int64ul, Padding, PaddedString

CCitadelPlayerController = Struct(
    Padding(0x6BC),
    "m_hPawn" / Int32ul,  # CHandle<C_BasePlayerPawn>
    Padding(0x30),
    "m_iszPlayerName" / PaddedString(0x80, "utf8"),
    Padding(0x8),
    "m_steamID" / Int64ul,
    "m_bIsLocalPlayerController" / Int8ul,
    "m_bNoClipEnabled" / Int8ul,
    Padding(0x16E),
    "m_PlayerDataGlobal" / PlayerDataGlobal,
    # Useful? Maybe good for enemy player yaw
    # self.m_hHeroPawn = int.from_bytes(data[0x8AC:0x8B0], byteorder="little")
)
