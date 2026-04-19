#!/usr/bin/env python3
"""
main.py
=======

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-03-08
Modification Date:     2026-04-19

"""

import logging
from pathlib import Path
import sys
from typing import Union

# pylint: disable=import-error,invalid-name
import memprocfs
import pygame
import pygame.freetype
from pygame.math import Vector2

from game import Game
from model import HeroID
from ui import MapUI

logging.basicConfig()
LOG = logging.getLogger()
LOG.setLevel("DEBUG")

MAP_BG = Path("images/minimap_mid_psd_7034a849.png")


def loadImages(ui: MapUI) -> None:
    ui.loadImage(MAP_BG, "map")
    loadedIconCount = 0

    for hero in HeroID:
        path = Path("images/icons") / f"{hero.name.lower()}.png"

        if path.exists():
            ui.loadImage(path, hero.name, (32, 32))
            loadedIconCount += 1

    LOG.info(f"Loaded {loadedIconCount} hero icons")


def main() -> int:
    # Check for physmemmap.txt
    vmmArgs = ["-device", "fpga"]

    if Path("physmemmap.txt").exists():
        vmmArgs += ["-memmap", "physmemmap.txt"]

    else:
        LOG.warning(
            "No physmmemmap.txt found. You may experience issues with an AMD"
            " CPU or thunderbolt-based DMA card."
        )

    vmm = memprocfs.Vmm(vmmArgs)
    proc = vmm.process("deadlock.exe")

    game = Game(proc)

    pygame.init()
    pygame.freetype.init()
    mapUI = MapUI(game.map.BottomLeft, game.map.TopRight)
    loadImages(mapUI)

    def _loop():
        if not game.update() or not game.localPlayerController:
            return

        localPawn = game.localPlayerController.pawn

        mapUI.clear()

        for player in game.playerControllers:
            label = [
                f"{player.m_iszPlayerName} [{player.pawn.m_iHealth}]",
            ]
            mapUI.add(
                MapUI.Element(
                    Vector2(
                        player.pawn.gameSceneNode.m_vecAbsOrigin[0],
                        player.pawn.gameSceneNode.m_vecAbsOrigin[1],
                    ),
                    player.pawn.m_iTeamNum == localPawn.m_iTeamNum,
                    label=label,
                    dead=(player.pawn.m_iHealth == 0),
                    healthPc=(
                        player.pawn.m_iHealth / player.m_PlayerDataGlobal.m_iHealthMax
                        if player.m_PlayerDataGlobal.m_iHealthMax
                        else None
                    ),
                    imageName=player.m_PlayerDataGlobal.m_nHeroID.name,
                    # FIXME: Always 0 for any player other than local
                    yaw=player.pawn.v_angle[1],
                )
            )

        mapUI.draw(reflect=localPawn.m_iTeamNum == 3)

        # LOG.debug(
        #     "\n".join(
        #         (
        #             f"pos: {localPawn.gameSceneNode.m_vecAbsOrigin} ang: {localPawn.v_angle}",
        #             # f"Hero: {ourController.m_PlayerDataGlobal.m_nHeroID.name}",
        #             # f"Health: {pawn.m_iHealth}/{pawn.m_iMaxHealth}",
        #             # f"LifeState: {pawn.m_lifeState}",
        #             # f"Velocity: {pawn.vecAbsVelocity}",
        #         )
        #     )
        # )

    try:
        while True:
            _loop()

    except:
        pygame.quit()
        pygame.freetype.quit()

        raise

    return 0


if __name__ == "__main__":
    sys.exit(main())
