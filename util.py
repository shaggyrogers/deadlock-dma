#!/usr/bin/env python3
"""
util.py
=======

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-12
Modification Date:     2026-04-12

"""

from itertools import batched
import logging
from typing import Union

import memprocfs

LOG = logging.getLogger()
LOG.setLevel("DEBUG")


def scanSig(
    proc: "memprocfs.VmmProcess", sig: str, module: Union[str, None] = None
) -> int:
    """Scan for a signature, optionally limited to a specific module (e.g. "example.dll"), returning the address of the first match.

    Signatures look like this: 40 eb 17 ?? ?? ?? ?? cf ff
    Where each pair of characters is a known byte (hex) and ?? is an unknown/wildcard byte.
    Spaces are optional and will be ignored.
    """
    # TODO: Maybe limit to executable memory only?
    sig = sig.replace(" ", "").lower()

    # Validate sig
    assert len(sig) % 2 == 0
    assert sig.replace("?", "x").isalnum()

    # Make bitmask
    mask = "".join("f" if byte == "?" else "0" for byte in sig)

    if module:
        module = proc.module(module)

    # Scan
    # TODO: Search strategy?
    # TODO: Check for, fail if multiple matches?
    # FIXME: module.base + module.image_size is not correct but close enough
    search = proc.search(
        module.base if module else 0,
        (module.base + module.image_size) if module else 0xFFFFFFFFFFFFFFFF,
        memprocfs.FLAG_NOCACHE,
    )
    search.max_results = 1
    search.add_search(
        bytes(int(b[0] + b[1], base=16) for b in batched(sig.replace("?", "0"), 2)),
        bytes(int(b[0] + b[1], base=16) for b in batched(mask, 2)),
        1,
    )
    search.start()

    LOG.debug(f"Scanning, sig={sig} mask={mask}")
    result = search.result()

    if not result:
        raise ValueError(f"No matches found for signature: '{sig}'")

    result = result[0][0]
    LOG.debug(f"Found result at addr: 0x{result:02X}:")

    return result
