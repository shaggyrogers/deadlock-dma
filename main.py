#!/usr/bin/env python3
"""
main.py
=======

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-03-08
Modification Date:     2026-04-15

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
from ui import RadarUI

logging.basicConfig()
LOG = logging.getLogger()
LOG.setLevel("DEBUG")


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
    radar = RadarUI()

    def _loop():
        game.update()

        if not game.localPlayerController:
            return

        localPawn = game.localPlayerController.pawn

        radar.clear()

        for player in game.playerControllers:
            label = [
                player.m_iszPlayerName,
                (
                    f"{player.m_PlayerDataGlobal.m_nHeroID.name}"
                    + f" ({player.pawn.m_iHealth/player.m_PlayerDataGlobal.m_iHealthMax:.0%})"
                ),
            ]
            radar.add(
                RadarUI.RadarElem(
                    Vector2(
                        player.pawn.gameSceneNode.m_vecAbsOrigin[0],
                        player.pawn.gameSceneNode.m_vecAbsOrigin[1],
                    ),
                    player.pawn.m_iTeamNum == localPawn.m_iTeamNum,
                    label=label,
                    dead=(player.pawn.m_iHealth == 0),
                )
            )

        radar.draw(
            Vector2(
                localPawn.gameSceneNode.m_vecAbsOrigin[0],
                localPawn.gameSceneNode.m_vecAbsOrigin[1],
            ),
            localPawn.v_angle[1],
        )

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
