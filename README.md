# README

DMA cheat for Deadlock. WIP, currently provides radar only.

## Requirements

You will need:

* DMA card supported by PCILeech
* Python 3.12 (3.7+ will probably work)
  - uv
* Slave PC and master laptop to run the game and cheat respectively

## Setup

If you are using an AMD CPU and/or Thunderbolt-based DMA card, generate a `physmemmap.txt` using [the instructions here](https://github.com/ufrisk/LeechCore/wiki/Device_FPGA_AMD_Thunderbolt) and place it in the project root directory.

# Usage

Install missing dependencies and run:

`uv run python main.py`
