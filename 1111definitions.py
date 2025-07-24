# definitions.py
#
# 这是完全由数据驱动的Netlink Vendor Subcmd解析规则定义文件。
#
# ========================
# --- 格式规范 (v2.0) ---
# ========================
#
# ... (之前的规范保持不变) ...
#
# 新增模式：如何定义重复项列表 (e.g., 频率列表, SSID列表)
#
# 1. 为列表创建一个新的专属属性规则集 (e.g., "frequency_list_attrs")。
# 2. 在这个新规则集中，使用通配符 "*" 来定义列表中每一项的统一名称。
#    例如: "frequency_list_attrs": { "*": "Frequency" }
# 3. 在 "nested_rules" 中，将触发此列表的 type_id 指向这个新的规则集名称。
#    例如: "nested_rules": { "attrs": { 2: "frequency_list_attrs" } }
#
# ========================

VENDOR_SUBCMD_ENUMS = {
        # 新增一个顶层 "structs" 字典，用于定义所有自定义二进制结构体
    "structs": {
        "sta_flag_update": [
            # 这是一个有序列表，定义了字段名和它们的类型
            ("mask", "u32"),
            ("set", "u32")
        ]
    },
    107: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_SCAN_DONE",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_INVALID_PARAM', 'type': 'hex'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_IE', 'type': 'hex'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_FREQUENCIES', 'type': 'hex'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_SSIDS', 'type': 'hex'},
                4: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_SUPP_RATES', 'type': 'hex'},
                5: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_TX_NO_CCK_RATE', 'type': 'u8'},
                6: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_FLAGS', 'type': 'u32'},
                7: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_COOKIE', 'type': 'u64'},
                8: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_STATUS', 'type': 'u8'},
                9: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_MAC', 'type': 'hex'},
                10: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_MAC_MASK', 'type': 'hex'},
                11: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_BSSID', 'type': 'hex'},
                12: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_DWELL_TIME', 'type': 'u32'},
                13: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_PRIORITY', 'type': 'u8'},
                14: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_AFTER_LAST', 'type': 'u8'}
                 },
        # 新增的、专门用于解释列表内容的规则集
        "frequency_list_attrs": {
            "*": "Frequency"
        },
        "ssid_list_attrs": { 
            "*": { "name": "SSID", "type": "string" } 
        }, # SSID列表中的每一项都是字符串
        "nested_rules": {
            "attrs": {
                2: "frequency_list_attrs",  # 遇到Type 2嵌套，切换到频率列表规则
                3: "ssid_list_attrs"        # 遇到Type 3嵌套，切换到SSID列表规则
            }
        }
    },
    65025: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_START_AP",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_CONTAINER', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_FREQ', 'type': 'u32'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_BW', 'type': 'u32'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_SSID', 'type': 'string'},
                4: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_FLAGS', 'type': 'u8'},
                5: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_RESULT', 'type': 'u32'},
                6: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_IFNAME', 'type': 'string'}
                }
    },
    165: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WLAN_MAC_INFO",
        "initial_rule": "mac_attrs",
        "mac_attrs": { 1: "QCA_WLAN_VENDOR_ATTR_MAC_INFO" },
        "mac_id_attrs": { "*": "MAC_ID_CONTAINER" },
        "attrs": {
            1: "QCA_WLAN_VENDOR_ATTR_MAC_INFO_MAC_ID",
            2: "QCA_WLAN_VENDOR_ATTR_MAC_INFO_BAND",
            3: "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO",
        },
        "iface_container_attrs": { "*": "INTERFACE_CONTAINER"},
        "iface_info_attrs": {
            1: "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO_IFINDEX",
            2: "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO_FREQ",
            3: "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO_IFTYPE",
        },
        "nested_rules": {
            "mac_attrs":           { 1: "mac_id_attrs" },
            "mac_id_attrs":        { "*": "attrs" },
            "attrs":               { 3: "iface_container_attrs" },
            "iface_container_attrs": { "*": "iface_info_attrs" }
        }
    },
    65026: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_ADD_VIF",
        "initial_rule": "attrs",
        "attrs": {
            0: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_ADD_VIF_CONTAINER",
            1: "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_IFNAME",
            2: "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_IFTYPE",
            3: "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_NAME_ASSIGN_TYPE",
            4: "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_FLAGS",
            5: "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_MAC_ADDR",
            6: "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_RESULT",
        }
    },
    181: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_INTEROP_ISSUES_AP",
        "initial_rule": "attrs",
        "attrs": {
            0: "QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_CONTAINER",
            1: "QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_TYPE",
            2: "QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_LIST",
            3: "QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_BSSID",
        }
    },
    12: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_NAN",
        "initial_rule": "attrs",
        "attrs": {
            # 根据C代码，subcmd 12只包含一个属性。
            # 经过查阅内核代码，QCA_WLAN_VENDOR_ATTR_NAN 的 type_id 通常是 2。
            # 我们将它定义为一个普通的、非嵌套的属性。
            2: "QCA_WLAN_VENDOR_ATTR_NAN_DATA_BLOB"
        }
        # 注意：这里没有 nested_rules，因为我们不希望解析器进入这个属性的内部。
    },
    54: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_DO_ACS",
        "initial_rule": "attrs",
        "attrs": {
            0: "QCA_WLAN_VENDOR_ATTR_ACS_CHANNEL_CONTAINER",
            1: "QCA_WLAN_VENDOR_ATTR_ACS_PRIMARY_CHANNEL",
            2: "QCA_WLAN_VENDOR_ATTR_ACS_SECONDARY_CHANNEL",
            3: "QCA_WLAN_VENDOR_ATTR_ACS_HW_MODE",
            4: "QCA_WLAN_VENDOR_ATTR_ACS_HT_ENABLED",
            5: "QCA_WLAN_VENDOR_ATTR_ACS_HT40_ENABLED",
            6: "QCA_WLAN_VENDOR_ATTR_ACS_VHT_ENABLED",
            7: "QCA_WLAN_VENDOR_ATTR_ACS_CHWIDTH",
            8: "QCA_WLAN_VENDOR_ATTR_ACS_CH_LIST",
            9: "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG0_CENTER_CHANNEL",
            10: "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG1_CENTER_CHANNEL",
            11: "QCA_WLAN_VENDOR_ATTR_ACS_FREQ_LIST",
            12: "QCA_WLAN_VENDOR_ATTR_ACS_PRIMARY_FREQUENCY",
            13: "QCA_WLAN_VENDOR_ATTR_ACS_SECONDARY_FREQUENCY",
            14: "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG0_CENTER_FREQUENCY",
            15: "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG1_CENTER_FREQUENCY",
            16: "QCA_WLAN_VENDOR_ATTR_ACS_EDMG_ENABLED",
            17: "QCA_WLAN_VENDOR_ATTR_ACS_EDMG_CHANNEL",
            18: "QCA_WLAN_VENDOR_ATTR_ACS_PUNCTURE_BITMAP",
            19: "QCA_WLAN_VENDOR_ATTR_ACS_EHT_ENABLED",
            20: "QCA_WLAN_VENDOR_ATTR_ACS_LAST_SCAN_AGEOUT_TIME",
        }
    },
    106:{   
        "name": "QCA_NL80211_VENDOR_SUBCMD_TRIGGER_SCAN",
        "initial_rule": "attrs",
        "attrs": {
            0: "QCA_WLAN_VENDOR_ATTR_SCAN_INVALID_PARAM",
            1: "QCA_WLAN_VENDOR_ATTR_SCAN_IE",
            2: "QCA_WLAN_VENDOR_ATTR_SCAN_FREQUENCIES",
            3: "QCA_WLAN_VENDOR_ATTR_SCAN_SSIDS",
            4: "QCA_WLAN_VENDOR_ATTR_SCAN_SUPP_RATES",
            5: "QCA_WLAN_VENDOR_ATTR_SCAN_TX_NO_CCK_RATE",
            6: "QCA_WLAN_VENDOR_ATTR_SCAN_FLAGS",
            7: "QCA_WLAN_VENDOR_ATTR_SCAN_COOKIE",
            8: "QCA_WLAN_VENDOR_ATTR_SCAN_STATUS",
            9: "QCA_WLAN_VENDOR_ATTR_SCAN_MAC",
            10: "QCA_WLAN_VENDOR_ATTR_SCAN_MAC_MASK",
            11: "QCA_WLAN_VENDOR_ATTR_SCAN_BSSID",
            12: "QCA_WLAN_VENDOR_ATTR_SCAN_DWELL_TIME",
            13: "QCA_WLAN_VENDOR_ATTR_SCAN_PRIORITY",
            14: "QCA_WLAN_VENDOR_ATTR_SCAN_AFTER_LAST",
        },
        # 新增的、专门用于解释列表内容的规则集
        "frequency_list_attrs": {
            "*": "Frequency"
        },
        "ssid_list_attrs": { 
            "*": { "name": "SSID", "type": "string" } 
        }
    },
    65032: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_CHANGE_BSS",
        "initial_rule": "attrs",
        "attrs": {
            0: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_INVALID",
            1: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_IFNAME",
            2: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_VDEV_ID",
            3: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_DEVICE_MODE",
            4: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_AP_ISOLATE",
            5: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_RESULT",
        }
    },
    65036: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_DEL_STATION",
        "initial_rule": "attrs",
        "attrs": {
            0: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_INVALID",
            1: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_IFNAME",
            2: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_VDEV_ID",
            3: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_DEVICE_MODE",
            4: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_MAC",
            5: "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_RESULT",
        }
    },
    # --- SubCmd Definitions ---
    101: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_LINK_PROPERTIES",
        "initial_rule": "attrs",
        "attrs": {
            # 将STA_FLAGS定义为一个需要进一步解析的“嵌套”属性
            5: "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_STA_FLAGS", 
            4: { "name": "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_MAC_ADDR", "type": "mac_address" }
        },
        # 定义一个专门用于解析sta_flag_update结构体的规则集
        # 这里的键是二进制数据中的偏移量（offset）
        "sta_flag_update_attrs": {
            0: { "name": "mask", "type": "u32" },
            4: { "name": "set", "type": "u32" }
        },
        "nested_rules": {
            # 定义转换规则：当遇到type_id为5的属性时，用sta_flag_update_attrs规则来解析它的payload
            "attrs": {
                5: "sta_flag_update_attrs"
            }
        }
    }
}