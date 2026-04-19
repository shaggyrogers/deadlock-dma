# README

DMA cheat for Deadlock. WIP, currently provides radar only.

## Requirements

You will need:

* DMA card supported by PCILeech
* Python 3.12+
  - uv
* Slave PC and master laptop to run the game and cheat respectively

## Setup

If you are using an AMD CPU and/or Thunderbolt-based DMA card, it may be necessary to generate a `physmemmap.txt` using [the instructions here](https://github.com/ufrisk/LeechCore/wiki/Device_FPGA_AMD_Thunderbolt) and place it in the project root directory.

To use [flameblast12's hero icons](https://www.reddit.com/r/DeadlockTheGame/comments/1qln47n/deadlock_dota_styled_pixel_minimap_iconsold_god/) for the minimap, follow instructions in `gen_hero_icons.py`.

# Usage

Install missing dependencies and run:

`uv run python main.py`
