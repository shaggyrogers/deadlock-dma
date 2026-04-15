#!/usr/bin/env python3
"""
CCitadelPlayerController.py
===========================

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-08
Modification Date:     2026-04-12

"""

from .PlayerDataGlobal import PlayerDataGlobal


class CCitadelPlayerController:
    """ """

    # Would be nice to just be able to do len(SomeClass)
    SIZE = 0xC30

    def __init__(self, data: bytes) -> None:
        """Initialises a CCitadelPlayerController instance."""
        # FIXME: look at Construct or cstructimpl

        self.pawn = None
        self.m_hPawn = int.from_bytes(data[0x6BC:0x6C0], byteorder="little")

        bName = data[0x6F0:0x770]
        self.m_iszPlayerName = bName[: bName.find(b"\x00")].decode("utf-8")

        # Useful?
        # self.m_hHeroPawn = int.from_bytes(data[0x8AC:0x8B0], byteorder="little")

        self.m_PlayerDataGlobal = PlayerDataGlobal(
            data[0x8F0 : 0x8F0 + PlayerDataGlobal.SIZE]
        )
