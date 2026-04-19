#!/usr/bin/env python3
"""
ui.py
=====

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-03-19
Modification Date:     2026-04-19

"""

import logging
from typing import Union

import pygame
import pygame.freetype
import pygame.image
import pygame.transform
from pygame.math import Vector2
from pygame import Rect

logging.basicConfig()
LOG = logging.getLogger()
LOG.setLevel("DEBUG")


class MapUI:
    class Element:
        """Player or other object to be drawn"""

        def __init__(
            self,
            pos: Vector2,
            friendly: bool,
            label: Union[str, list, None] = None,
            dead: Union[bool, None] = False,
            healthPc: Union[float, None] = None,  # [0, 1]
            imageName: Union[str, None] = None,
            yaw: Union[float, None] = None,
        ) -> None:
            self.pos = pos
            self.friendly = friendly
            self.label = label
            self.dead = dead
            self.healthPc = healthPc
            self.imageName = imageName
            self.yaw = yaw

    def __init__(self, bottomLeft: tuple[int, int], topRight: tuple[int, int]) -> None:
        """Initialise map given bounds"""
        self._bottomLeft = Vector2(*bottomLeft)
        self._topRight = Vector2(*topRight)

        self.elems = []

        self._bgColor = "#263238"
        self._enemyColor = "#d02222"
        self._friendlyColor = "#22d022"
        self._deadColor = "#7c7ca0"

        self._screen = pygame.display.set_mode((1080, 1080))
        self._font = pygame.freetype.SysFont("Sans", 16)

        self._images = {}

    def clear(self) -> None:
        """Clear all radar elements."""
        self.elems = []

    def add(self, elem: Element) -> None:
        """Add a radar element."""
        self.elems.append(elem)

    def loadImage(
        self, path: str, name: str, scaleTo: Union[tuple[int], None] = None
    ) -> None:
        """Load image and associate it with a name."""
        img = pygame.image.load(path)

        if scaleTo:
            img = pygame.transform.scale(img, scaleTo)

        self._images[name] = img

    def _convertPosition(self, targetPos: Vector2, reflect: bool) -> Vector2:
        """Convert world position to screen position."""
        targetPos = Vector2(
            (targetPos.x - self._bottomLeft.x)
            / (self._topRight.x - self._bottomLeft.x),
            1
            - (targetPos.y - self._bottomLeft.y)
            / (self._topRight.y - self._bottomLeft.y),
        )

        if reflect:
            targetPos.y = 1 - targetPos.y
            targetPos.x = 1 - targetPos.x

        size = Vector2(self._screen.get_width(), self._screen.get_height())

        return targetPos * self._screen.get_width()

    def draw(self, reflect: bool) -> None:
        """Draw the radar.

        If reflect is True, all player positions are mirrored.
        """

        self._screen.fill(self._bgColor)

        assert "map" in self._images
        self._screen.blit(
            self._images["map"],
            Rect(
                0,
                0,
                self._screen.get_width(),
                self._screen.get_height(),
            ),
        )

        for elem in self.elems:
            self._drawPlayer(elem, reflect)

        pygame.display.flip()

    def _drawPlayer(self, player: Element, reflect: bool) -> None:
        pos = self._convertPosition(player.pos, reflect)

        if player.dead:
            color = self._deadColor

        elif player.friendly:
            color = self._friendlyColor

        else:
            color = self._enemyColor

        pygame.draw.circle(self._screen, color, pos, 8)

        # FIXME: Yaw only set for local player
        # if player.yaw is not None:
        #     # TODO: change to triangle or view cone
        #     pygame.draw.line(
        #         self._screen,
        #         color,
        #         pos,
        #         # ?
        #         Vector2(32, 0).rotate(-player.yaw + (0 if reflect else 180)) + pos,
        #     )

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
                )

                offset += 22

        if player.imageName and player.imageName in self._images:
            img = self._images[player.imageName]
            self._screen.blit(
                img,
                Rect(
                    pos.x - int(img.get_width() / 2),
                    pos.y - int(img.get_height() / 2),
                    img.get_width(),
                    img.get_height(),
                ),
            )

        if player.healthPc is not None:
            if not 0 <= player.healthPc <= 1:
                # This happens sometimes if max health is updated late.
                LOG.warn(
                    f"Player {player.label} with invalid healthPc {player.healthPc}"
                )

                return

            # Lighter grey bg, bar fade between green and red
            g = int(255 * player.healthPc)
            r = int(255 * (1 - player.healthPc))

            pygame.draw.rect(
                self._screen,
                "#999999",
                Rect(pos.x - 16, pos.y - 16, 6, 38),
                width=4,
            )
            pygame.draw.rect(
                self._screen,
                f"#{r:02X}{g:02X}00",
                Rect(pos.x - 16, pos.y - 16, 6, int(38 * player.healthPc)),
                width=4,
            )
