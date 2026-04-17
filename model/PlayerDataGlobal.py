#!/usr/bin/env python3
"""
PlayerDataGlobal.py
===================

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-11
Modification Date:     2026-04-17

"""

from construct import Adapter, Struct, Int8ul, Int32ul, Float32l, Padding

from .HeroID import HeroID


class HeroIDAdapter(Adapter):
    # pylint: disable=unused-argument
    def _decode(self, obj, ctx, path) -> HeroID:
        return HeroID(obj)

    def _encode(self, obj: HeroID, ctx, path) -> int:
        return obj.value


PlayerDataGlobal = Struct(
    Padding(0x8),
    "m_iLevel" / Int32ul,
    "m_iMaxAmmo" / Int32ul,
    "m_iHealthMax" / Int32ul,
    "m_flHealthRegen" / Float32l,
    "m_flRespawnTime" / Float32l,
    "m_nHeroID" / HeroIDAdapter(Int32ul),
    "m_unHeroBadgeXP" / Int32ul,  # HeroBadgeXP_t
    "m_iGoldNetWorth" / Int32ul,
    "m_iAPNetWorth" / Int32ul,
    "m_iCreepGold" / Int32ul,
    "m_iCreepGoldSoloBonus" / Int32ul,
    "m_iCreepGoldKill" / Int32ul,
    "m_iCreepGoldAirOrb" / Int32ul,
    "m_iCreepGoldGroundOrb" / Int32ul,
    "m_iCreepGoldDeny" / Int32ul,
    "m_iCreepGoldNeutral" / Int32ul,
    "m_iFarmBaseline" / Int32ul,
    "m_iHealth" / Int32ul,
    "m_iPlayerKills" / Int32ul,
    "m_iPlayerAssists" / Int32ul,
    "m_iDeaths" / Int32ul,
    "m_iDenies" / Int32ul,
    "m_iLastHits" / Int32ul,
    "m_iKillStreak" / Int32ul,
    "m_bAlive" / Int8ul,
    "m_nHeroDraftPosition" / Int32ul,
    "m_bUltimateTrained" / Int8ul,
    "m_flUltimateCooldownStart" / Float32l,  # GameTime_t
    "m_flUltimateCooldownEnd" / Float32l,  # GameTime_t
    "m_bHasRejuvenator" / Int8ul,
    "m_bHasRebirth" / Int8ul,
    "m_bFlaggedAsCheater" / Int8ul,
    "m_iHeroDamage" / Int32ul,
    "m_iHeroHealing" / Int32ul,
    "m_iSelfHealing" / Int32ul,
    "m_iObjectiveDamage" / Int32ul,
    # TODO
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
)
