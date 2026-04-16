#!/usr/bin/env python3
"""
gen_hero_icons.py
=================

Description:           Separate flameblast12's deadlock hero icons
Author:                Michael De Pasquale
Creation Date:         2026-04-16
Modification Date:     2026-04-16

Usage
-----
1. Download and save the following image to the project directory:
    https://www.reddit.com/r/DeadlockTheGame/comments/1qln47n/deadlock_dota_styled_pixel_minimap_iconsold_god/

2. Remove the background using gimp/photoshop/etc

3. Run this script

"""

from pathlib import Path

from PIL import Image

# Names in order they appear
NAMES = [
    "abrams",
    "bebop",
    "billy",
    "calico",
    "doorman",
    "drifter",
    "dynamo",
    "greytalon",
    "haze",
    "holliday",
    "infernus",
    "ivy",
    "kelvin",
    "ladygeist",
    "lash",
    "mcginnis",
    "mina",
    "mirage",
    "moandkrill",
    "paige",
    "paradox",
    "pocket",
    "seven",
    "shiv",
    "sinclair",
    "victor",
    "vindicta",
    "viscous",
    "vyper",
    "warden",
    "wraith",
    "yamato",
    "hiddenking",
    "apollo",
    "celeste",
    "graves",
    "rem",
    "silver",
    "venator",
    "archmother",
]


iconDir = Path("images/icons")
iconDir.mkdir(parents=True, exist_ok=True)

img = Image.open(
    "deadlock-dota-styled-pixel-minimap-icons-old-god-new-blood-v0-pb1ebta2vafg1.webp"
)

size = (116, 119)
y = 26

for yIdx in range(5):
    x = 28

    for xIdx in range(8):
        name = NAMES[yIdx * 8 + xIdx]
        img.crop((x, y, x + size[0], y + size[1])).save(iconDir / (name + ".png"))
        x += size[0] + 13

    y += size[1] + 10
