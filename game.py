#!/usr/bin/env python3
"""
game.py
=======

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-12
Modification Date:     2026-04-19

"""

import logging
import struct
import time
from typing import Union

import construct.core
import memprocfs

from model import CCitadelPlayerController, CCitadelPlayerPawn, CGameSceneNode
from util import scanSig

LOG = logging.getLogger()
LOG.setLevel("DEBUG")


class Map:
    BottomLeft = (-9597, -10842)
    TopRight = (9179, 11090)


class Game:

    def __init__(self, proc: "memprocfs.VmmProcess") -> None:
        self._process = proc

        self._dwEntityList = self._getDwEntityList()
        self._dwLocalPlayer = self._getDwLocalPlayer()

        self.localPlayerController: CCitadelPlayerController = None
        self.playerControllers = []

        self._lastValidLocalPlayerTime = float("-inf")

        self.map = Map

    def update(self) -> None:
        self.localPlayerController = self._getController(self._dwLocalPlayer)
        self._updatePlayers()

        # If we haven't been able to get a valid local CCitadelPlayerController in
        # a while, update offsets
        if self.localPlayerController:
            self._lastValidLocalPlayerTime = time.monotonic()

        if time.monotonic() - self._lastValidLocalPlayerTime > 5:
            self._dwEntityList = self._getDwEntityList()
            self._dwLocalPlayer = self._getDwLocalPlayer()
            self._lastValidLocalPlayerTime = time.monotonic()

        return True

    def _updatePlayers(self) -> None:
        result = []

        for i in range(64):
            if not (ent := self._getEntity(i)):
                continue

            # FIXME: Properly check for CCitadelPlayerController?
            controller = self._getController(ent)

            if controller:
                result.append(controller)

        self.playerControllers = result

    def _getController(self, controller: int) -> Union[CCitadelPlayerController, None]:
        """Read and build CCitadelPlayerController from pointer. Returns None if
        unsuccessful.
        """
        try:
            controller = CCitadelPlayerController.parse(
                self._process.memory.read(
                    controller,
                    CCitadelPlayerController.sizeof(),
                    memprocfs.FLAG_NOCACHE,
                )
            )

        except (ValueError, construct.core.StringError, construct.core.StreamError):
            return None

        if not controller.m_hPawn:
            return None

        pPawn = self._getEntity(controller.m_hPawn)

        if not pPawn:
            return None

        controller.pawn = CCitadelPlayerPawn.parse(
            self._process.memory.read(
                pPawn, CCitadelPlayerPawn.sizeof(), memprocfs.FLAG_NOCACHE
            )
        )

        if not controller.pawn.m_pGameSceneNode:
            return None

        controller.pawn.gameSceneNode = CGameSceneNode.parse(
            self._process.memory.read(
                controller.pawn.m_pGameSceneNode,
                CGameSceneNode.sizeof(),
                memprocfs.FLAG_NOCACHE,
            )
        )

        return controller

    def _getEntity(self, handle: int) -> int:
        # Names?
        controller = int.from_bytes(
            self._process.memory.read(
                self._dwEntityList + 0x10 + 0x8 * ((handle & 0x3FFF) >> 0x9),
                8,
                memprocfs.FLAG_NOCACHE,
            ),
            byteorder="little",
        )

        # LOG.debug(f"controller = 0x{controller:02X}")

        if not controller:
            return None

        entity = int.from_bytes(
            self._process.memory.read(
                controller + 0x70 * (handle & 0x1FF), 8, memprocfs.FLAG_NOCACHE
            ),
            byteorder="little",
        )

        # LOG.debug(f"entity = 0x{entity:02X}")

        return entity

    def _getDwEntityList(self) -> int:
        # https://www.unknowncheats.me/forum/deadlock/639185-deadlock-reversal-structs-offsets-57.html
        addr = scanSig(
            self._process,
            "48 8B 0D ?? ?? ?? ?? 48 89 7C 24 ?? 8B FA C1 EB",
            "client.dll",
        )
        assert addr

        pDwEntityList = (
            addr
            + 7
            + int.from_bytes(
                self._process.memory.read(addr, 7)[3:7], byteorder="little"
            )
        )
        dwEntityList = int.from_bytes(
            self._process.memory.read(pDwEntityList, 8), byteorder="little"
        )
        LOG.debug(f"dwEntityList = 0x{dwEntityList:02X}")

        return dwEntityList

    def _getDwLocalPlayer(self) -> int:
        addr = scanSig(
            self._process, "48 8D 0D ?? ?? ?? ?? 33 FF 48 89 34 D9", "client.dll"
        )
        assert addr

        pDwLocalPlayer = (
            addr
            + 7
            + int.from_bytes(
                self._process.memory.read(addr, 7)[3:7], byteorder="little"
            )
        )
        dwLocalPlayer = int.from_bytes(
            self._process.memory.read(pDwLocalPlayer, 8), byteorder="little"
        )
        LOG.debug(f"dwLocalPlayer = 0x{dwLocalPlayer:02X}")

        return dwLocalPlayer
