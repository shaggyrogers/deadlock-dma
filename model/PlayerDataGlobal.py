#!/usr/bin/env python3
"""
PlayerDataGlobal.py
===================

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-11
Modification Date:     2026-04-12

"""

import struct

from .HeroID import HeroID


class PlayerDataGlobal:
    """Docstring for PlayerDataGlobal:."""

    SIZE = 0x330

    def __init__(self, data: bytes) -> None:
        """Initialises a PlayerDataGlobal: instance."""

        # -> does setting FlaggedAsCheater turn people into frogs locally?

        self.m_iLevel = int.from_bytes(data[0x8 : 0x8 + 4], byteorder="little")

        # This is always 0, at least in hideout...
        self.m_iMaxAmmo = int.from_bytes(data[0xC : 0xC + 4], byteorder="little")
        self.m_iHealthMax = int.from_bytes(data[0x10 : 0x10 + 4], byteorder="little")

        self.m_flHealthRegen = struct.unpack("f", data[0x14 : 0x14 + 4])[0]
        self.m_flRespawnTime = struct.unpack("f", data[0x18 : 0x18 + 4])[
            0
        ]  # GameTime_t
        self.m_nHeroID = HeroID(
            int.from_bytes(data[0x1C : 0x1C + 4], byteorder="little")
        )  # HeroID_t

        # m_unHeroBadgeXP = 0x20(HeroBadgeXP_t, 4)[MNetworkEnable]

        self.m_iGoldNetWorth = int.from_bytes(data[0x24 : 0x24 + 4], byteorder="little")
        self.m_iAPNetWorth = int.from_bytes(data[0x28 : 0x28 + 4], byteorder="little")

        self.m_iCreepGold = int.from_bytes(data[0x2C : 0x2C + 4], byteorder="little")
        self.m_iCreepGoldSoloBonus = int.from_bytes(
            data[0x30 : 0x30 + 4], byteorder="little"
        )
        self.m_iCreepGoldKill = int.from_bytes(
            data[0x34 : 0x34 + 4], byteorder="little"
        )
        self.m_iCreepGoldAirOrb = int.from_bytes(
            data[0x38 : 0x38 + 4], byteorder="little"
        )
        self.m_iCreepGoldGroundOrb = int.from_bytes(
            data[0x3C : 0x3C + 4], byteorder="little"
        )
        self.m_iCreepGoldDeny = int.from_bytes(
            data[0x40 : 0x40 + 4], byteorder="little"
        )
        self.m_iCreepGoldNeutral = int.from_bytes(
            data[0x44 : 0x44 + 4], byteorder="little"
        )

        self.m_iFarmBaseline = int.from_bytes(data[0x48 : 0x48 + 4], byteorder="little")
        self.m_iHealth = int.from_bytes(data[0x4C : 0x4C + 4], byteorder="little")
        self.m_iPlayerKills = int.from_bytes(data[0x50 : 0x50 + 4], byteorder="little")
        self.m_iPlayerAssists = int.from_bytes(
            data[0x54 : 0x54 + 4], byteorder="little"
        )
        self.m_iDeaths = int.from_bytes(data[0x58 : 0x58 + 4], byteorder="little")
        self.m_iDenies = int.from_bytes(data[0x5C : 0x5C + 4], byteorder="little")
        self.m_iLastHits = int.from_bytes(data[0x60 : 0x60 + 4], byteorder="little")
        self.m_iKillStreak = int.from_bytes(data[0x64 : 0x64 + 4], byteorder="little")
        self.m_bAlive = data[0x68]
        self.m_nHeroDraftPosition = int.from_bytes(
            data[0x6C : 0x6C + 4], byteorder="little"
        )

        self.m_bUltimateTrained = data[0x70]

        # m_flUltimateCooldownStart = 0x74(GameTime_t, 4)[MNetworkEnable]
        # m_flUltimateCooldownEnd = 0x78(GameTime_t, 4)[MNetworkEnable]

        self.m_bHasRejuvenator = data[0x7C]
        self.m_bHasRebirth = data[0x7D]
        self.m_bFlaggedAsCheater = data[0x7E]

        self.m_iHeroDamage = int.from_bytes(data[0x80 : 0x80 + 4], byteorder="little")
        self.m_iHeroHealing = int.from_bytes(data[0x84 : 0x84 + 4], byteorder="little")
        self.m_iSelfHealing = int.from_bytes(data[0x88 : 0x88 + 4], byteorder="little")
        self.m_iObjectiveDamage = int.from_bytes(
            data[0x8C : 0x8C + 4], byteorder="little"
        )

        # m_vecUpgrades = 0x90 (C_NetworkUtlVectorBase< CUtlStringToken >, 24) [MNetworkEnable] [MNetworkUserGroup] [MNetworkChangeCallback]
        # m_vecBonusCounterAbilities = 0xA8 (C_NetworkUtlVectorBase< CUtlStringToken >, 24) [MNetworkEnable]
        # m_vecBonusCounterValues = 0xC0 (C_NetworkUtlVectorBase< int32 >, 24) [MNetworkEnable] [MNetworkUserGroup] [MNetworkChangeCallback]
        # m_vecBonusCounterModifiers = 0xD8 (C_NetworkUtlVectorBase< CUtlStringToken >, 24) [MNetworkEnable]
        # m_vecModifierBonusCounterValues = 0xF0 (C_NetworkUtlVectorBase< int32 >, 24) [MNetworkEnable] [MNetworkUserGroup] [MNetworkChangeCallback]
        # m_tHeldItem = 0x108 (CUtlStringToken, 4) [MNetworkEnable] [MNetworkUserGroup] [MNetworkChangeCallback]
        # m_vecImbuements = 0x110 (C_UtlVectorEmbeddedNetworkVar< ItemImbuementPair_t >, 104) [MNetworkEnable]
        # m_vecDynamicAbilityValues = 0x178 (C_UtlVectorEmbeddedNetworkVar< DynamicAbilityValues_t >, 104) [MNetworkEnable]
        # m_vecStatViewerModifierValues = 0x1E0 (C_UtlVectorEmbeddedNetworkVar< StatViewerModifierValues_t >, 104) [MNetworkEnable]
        # m_vecStolenAbilities = 0x248 (C_UtlVectorEmbeddedNetworkVar< StolenAbilityPair_t >, 104) [MNetworkEnable] [MNetworkUserGroup] [MNetworkChangeCallback]
        # m_vecAbilityUpgradeState = 0x2B0 (C_UtlVectorEmbeddedNetworkVar< AbilityUpgradeState_t >, 104) [MNetworkEnable] [MNetworkUserGroup] [MNetworkChangeCallback]
        # m_strIconHeroCardOverride = 0x318 (CUtlString, 8) [MNetworkEnable]
        # m_strIconHeroCardCriticalOverride = 0x320 (CUtlString, 8) [MNetworkEnable]
        # m_strIconHeroCardGloatOverride = 0x328 (CUtlString, 8) [MNetworkEnable]
