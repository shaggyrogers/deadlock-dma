#!/usr/bin/env python3
"""
ui.py
=====

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-03-19
Modification Date:     2026-04-15

"""

from typing import Union

import pygame
import pygame.freetype
from pygame.math import Vector2


class RadarUI:
    class RadarElem:
        def __init__(
            self,
            pos: Vector2,
            friendly: bool,
            label: Union[str, list, None] = None,
            dead: bool = False,
            healthPc: float = None,  # [0, 1]
        ) -> None:
            self.pos = pos
            self.friendly = friendly
            self.label = label
            self.dead = dead
            self.healthPc = healthPc

            if healthPc is not None:
                assert 0 <= healthPc <= 1

    def __init__(self) -> None:
        # Length of one side of radar square.
        self.maxDist = 16000

        self.elems = list()

        self._bgColor = "#263238"
        self._axisColor = "#455A64"
        self._axisWidth = 4

        self._enemyColor = "#d02222"
        self._friendlyColor = "#22d022"
        self._deadColor = "#7c7ca0"

        pygame.init()
        self._screen = pygame.display.set_mode((1080, 1080))
        self._font = pygame.freetype.SysFont("Sans", 16)

    def clear(self) -> None:
        """Clear all radar elements."""
        self.elems = []

    def add(self, elem: RadarElem) -> None:
        """Add a radar element."""
        self.elems.append(elem)

    def _convertPosition(
        self, playerPos: Vector2, playerYaw: float, targetPos: Vector2
    ) -> Vector2:
        """Convert world position to radar position."""
        targetPos = (targetPos - playerPos).rotate(-playerYaw - 90) / self.maxDist
        targetPos.x = -targetPos.x

        size = Vector2(self._screen.get_width(), self._screen.get_height())

        return targetPos * self._screen.get_width() / 2 + size / 2

    def draw(self, playerPos: Vector2, playerYaw: float) -> None:
        """Draw the radar."""
        self._screen.fill(self._bgColor)

        # Outline, axes
        size = min((self._screen.get_width(), self._screen.get_height()))

        pygame.draw.line(
            self._screen,
            self._axisColor,
            (size / 2, size),
            (size / 2, 0),
            self._axisWidth,
        )
        pygame.draw.line(
            self._screen,
            self._axisColor,
            (0, size / 2),
            (size, size / 2),
            self._axisWidth,
        )

        for elem in self.elems:
            self._drawPlayer(playerPos, playerYaw, elem)

        pygame.display.flip()

    def _drawPlayer(
        self,
        # TODO: Remove these, draw fixed entire map
        playerPos: Vector2,
        playerYaw: float,
        player: RadarElem,
    ) -> None:
        # TODO: Class icons
        pos = self._convertPosition(playerPos, playerYaw, player.pos)

        if player.dead:
            color = self._deadColor

        elif player.friendly:
            color = self._friendlyColor

        else:
            color = self._enemyColor

        pygame.draw.circle(self._screen, color, pos, 6)

        if player.label:
            if isinstance(player.label, str):
                player.label = [player.label]

            offset = 0

            for line in player.label[::-1]:
                self._font.render_to(
                    self._screen,
                    (pos.x - 8, pos.y - 28 - offset),
                    line,
                    fgcolor=color,
                    bgcolor=None,
                    # style=STYLE_DEFAULT, rotation=0, size=0
                )

                offset += 22
                assert player.healthPc is None


# Testing
if __name__ == "__main__":
    import time

    print("Running test")
    radar = RadarUI()

    for i in range(100):

        radar.clear()
        radar.add(RadarUI.RadarElem(Vector2(750 + i, 250 + i), True))
        radar.add(RadarUI.RadarElem(Vector2(850 + i, 600 + i), False))
        radar.add(RadarUI.RadarElem(Vector2(350 + i, 500 + i), False))

        radar.draw(Vector2(500, 500), 2 * i)
        time.sleep(0.05)
