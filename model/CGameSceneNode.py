#!/usr/bin/env python3
"""
CGameSceneNode.py
=================

Description:           TODO
Author:                Michael De Pasquale
Creation Date:         2026-04-12
Modification Date:     2026-04-16

"""

import struct


class CGameSceneNode:
    """Docstring for CGameSceneNode."""

    SIZE = 0x140

    def __init__(self, data: bytes) -> None:
        """Initialises a CGameSceneNode instance."""
        # m_bDirtyHierarchy = 0x0 (bitfield:1, 0) [MNotSaved]
        # m_bDirtyBoneMergeInfo = 0x0 (bitfield:1, 0) [MNotSaved]
        # m_bNetworkedPositionChanged = 0x0 (bitfield:1, 0) [MNotSaved]
        # m_bNetworkedAnglesChanged = 0x0 (bitfield:1, 0) [MNotSaved]
        # m_bNetworkedScaleChanged = 0x0 (bitfield:1, 0) [MNotSaved]
        # m_bWillBeCallingPostDataUpdate = 0x0 (bitfield:1, 0) [MNotSaved]
        # m_bBoneMergeFlex = 0x0 (bitfield:1, 0) [MNotSaved]
        # m_nLatchAbsOrigin = 0x0 (bitfield:2, 0) [MNotSaved]
        # m_bDirtyBoneMergeBoneToRoot = 0x0 (bitfield:1, 0) [MNotSaved]
        # m_nodeToWorld = 0x10 (CTransformWS, 32) [MNotSaved]

        # m_pOwner = 0x30 (CEntityInstance*, 8) [MNotSaved]
        # m_pParent = 0x38 (CGameSceneNode*, 8) [MNotSaved]
        # m_pChild = 0x40 (CGameSceneNode*, 8) [MNotSaved]
        # m_pNextSibling = 0x48 (CGameSceneNode*, 8) [MNotSaved]
        # m_hParent = 0x70 (CGameSceneNodeHandle, 16) [MNetworkEnable] [MNetworkSerializer] [MNetworkChangeCallback] [MNetworkPriority] [MNetworkVarEmbeddedFieldOffsetDelta]

        # m_vecOrigin = 0x80 (CNetworkOriginCellCoordQuantizedVector, 48) [MNetworkEnable] [MNetworkPriority] [MNetworkUserGroup] [MNetworkChangeCallback]
        self.m_angRotation = struct.unpack("3f", data[0xB8 : 0xB8 + 12])  # QAngle
        # m_flScale = 0xC4 (float32, 4) [MNetworkEnable] [MNetworkChangeCallback] [MNetworkPriority]
        self.m_vecAbsOrigin = struct.unpack("3f", data[0xC8 : 0xC8 + 12])  # VectorWS
        self.m_angAbsRotation = struct.unpack("3f", data[0xD4 : 0xD4 + 12])  # QAngle
        # m_flAbsScale = 0xE0 (float32, 4)

        # m_vecWrappedLocalOrigin = 0xE4 (Vector, 12) [MNotSaved]
        # m_angWrappedLocalRotation = 0xF0 (QAngle, 12) [MNotSaved]
        # m_flWrappedScale = 0xFC (float32, 4) [MNotSaved]
        # m_nParentAttachmentOrBone = 0x100 (int16, 2) [MNotSaved]
        # m_bDebugAbsOriginChanges = 0x102 (bool, 1) [MNotSaved]
        # m_bDormant = 0x103 (bool, 1)
        # m_bForceParentToBeNetworked = 0x104 (bool, 1)
        # m_nHierarchicalDepth = 0x107 (uint8, 1) [MNotSaved]
        # m_nHierarchyType = 0x108 (uint8, 1) [MNotSaved]
        # m_nDoNotSetAnimTimeInInvalidatePhysicsCount = 0x109 (uint8, 1) [MNotSaved]
        # m_name = 0x10C (CUtlStringToken, 4) [MNetworkEnable]
        # m_hierarchyAttachName = 0x120 (CUtlStringToken, 4) [MNetworkEnable] [MNetworkChangeCallback]
        # m_flClientLocalScale = 0x124 (float32, 4)

        self.m_vRenderOrigin = struct.unpack("3f", data[0x128 : 0x128 + 12])  # Vector
