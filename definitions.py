VENDOR_SUBCMD_ENUMS = {
    # ... 其他subcmd定义也需要更新为新格式 ...
    
    54: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_DO_ACS",
        "initial_rule": "attrs",
        "attrs": {
            # 完整定义，并为每个属性指定了明确的数据类型
            0:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_CHANNEL_CONTAINER", "type": "hex" },
            1:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_PRIMARY_CHANNEL", "type": "u8" },
            2:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_SECONDARY_CHANNEL", "type": "u8" },
            3:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_HW_MODE", "type": "u8" },
            4:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_HT_ENABLED", "type": "u8" },
            5:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_HT40_ENABLED", "type": "u8" },
            6:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_VHT_ENABLED", "type": "u8" },
            7:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_CHWIDTH", "type": "u16" }, # 明确指定为u16
            8:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_CH_LIST", "type": "hex" }, # 假设为字节流
            9:  { "name": "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG0_CENTER_CHANNEL", "type": "u8" },
            10: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG1_CENTER_CHANNEL", "type": "u8" },
            11: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_FREQ_LIST", "type": "hex" }, # 假设为字节流
            12: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_PRIMARY_FREQUENCY", "type": "u32" },
            13: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_SECONDARY_FREQUENCY", "type": "u32" },
            14: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG0_CENTER_FREQUENCY", "type": "u32" },
            15: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG1_CENTER_FREQUENCY", "type": "u32" },
            16: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_EDMG_ENABLED", "type": "u8" },
            17: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_EDMG_CHANNEL", "type": "u8" },
            18: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_PUNCTURE_BITMAP", "type": "u16" },
            19: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_EHT_ENABLED", "type": "u8" },
            20: { "name": "QCA_WLAN_VENDOR_ATTR_ACS_LAST_SCAN_AGEOUT_TIME", "type": "u32" },
        }
    },
    
    # 其他subcmd也需要按此格式更新...
    # 例如 subcmd 65025
    65025: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_START_AP",
        "initial_rule": "attrs",
        "attrs": {
            0: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_CONTAINER", "type": "nested" },
            1: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_FREQ", "type": "u32" },
            2: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_BW", "type": "u32" },
            3: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_SSID", "type": "string" },
            4: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_FLAGS", "type": "u32" },
            5: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_RESULT", "type": "s32" },
            6: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_IFNAME", "type": "string" },
        }
    },

    165: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WLAN_MAC_INFO",
        "initial_rule": "mac_attrs",
        "mac_attrs": {
            1: { "name": "QCA_WLAN_VENDOR_ATTR_MAC_INFO", "type": "nested" }
        },
        "mac_id_attrs": {
            "*": { "name": "MAC_ID_CONTAINER", "type": "nested" }
        },
        "attrs": {
            1: { "name": "QCA_WLAN_VENDOR_ATTR_MAC_INFO_MAC_ID", "type": "u32" },
            2: { "name": "QCA_WLAN_VENDOR_ATTR_MAC_INFO_BAND", "type": "u32" },
            3: { "name": "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO", "type": "nested" }
        },
        "iface_container_attrs": {
            "*": { "name": "INTERFACE_CONTAINER", "type": "nested" }
        },
        "iface_info_attrs": {
            1: { "name": "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO_IFINDEX", "type": "u32" },
            2: { "name": "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO_FREQ", "type": "u32" },
            3: { "name": "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO_IFTYPE", "type": "u32" }
        },
        "nested_rules": {
            "mac_attrs":           { 1: "mac_id_attrs" },
            "mac_id_attrs":        { "*": "attrs" },
            "attrs":               { 3: "iface_container_attrs" },
            "iface_container_attrs": { "*": "iface_info_attrs" }
        }
    },
     
    107: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_SCAN_DONE",
        "initial_rule": "attrs",
        "attrs": {
            0: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_INVALID_PARAM", "type": "u32" },
            1: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_IE", "type": "hex" },
            2: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_FREQUENCIES", "type": "nested" },
            3: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_SSIDS", "type": "nested" },
            4: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_SUPP_RATES", "type": "hex" },
            5: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_TX_NO_CCK_RATE", "type": "u8" },
            6: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_FLAGS", "type": "u8" },
            7: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_COOKIE", "type": "u64" },
            8: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_STATUS", "type": "u8" },
            9: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_MAC", "type": "mac_address" },
            10: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_MAC_MASK", "type": "mac_address" },
            11: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_BSSID", "type": "mac_address" },
            12: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_DWELL_TIME", "type": "u32" },
            13: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_PRIORITY", "type": "u32" },
            15: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_LINK_ID", "type": "u8" },
            16: { "name": "QCA_WLAN_VENDOR_ATTR_SCAN_SKIP_CHANNEL_RECENCY_PERIOD", "type": "u32" },
        },
        "frequency_list_attrs": {
            "*": { "name": "Frequency", "type": "u32" }
        },
        "ssid_list_attrs": { 
            "*": { "name": "SSID", "type": "string" } 
        },
        "nested_rules": {
            "attrs": {
                2: "frequency_list_attrs",
                3: "ssid_list_attrs"
            }
        }
    },

     101: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_LINK_PROPERTIES",
        "initial_rule": "attrs",
        "attrs": {
            # --- 这是核心修改 ---
            # 将 type_id 5 的类型标记为 "struct"，而不是 "nested"
            5: { "name": "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_STA_FLAGS", "type": "struct" },
            
            4: { "name": "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_MAC_ADDR", "type": "mac_address" }
        },
        # --- 这个定义现在描述了一个C结构体的内存布局 ---
        # 使用偏移量(0, 4)作为键
        "sta_flag_update_attrs": {
            0: { "name": "mask", "type": "u32" },
            4: { "name": "set", "type": "u32" }
        },
        # --- nested_rules 指明了当遇到 attrs[5] 时，应使用 sta_flag_update_attrs 规则 ---
        "nested_rules": {
            "attrs": {
                5: "sta_flag_update_attrs"
            }
        }
    },
        65026: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_ADD_VIF",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ADD_VIF_CONTAINER', 'type': 'u32'},
                1: {'name': 'QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_IFTYPE', 'type': 'u32'},
                3: {'name': 'QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_NAME_ASSIGN_TYPE', 'type': 'u32'},
                4: {'name': 'QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_FLAGS', 'type': 'u32'},
                5: {'name': 'QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_MAC_ADDR', 'type': 'mac_address'},
                6: {'name': 'QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_RESULT', 'type': 's32'}
                }
    },
    181: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_INTEROP_ISSUES_AP",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_CONTAINER', 'type': 'hex'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_TYPE', 'type': 'u32'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_LIST', 'type': 'u32'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_BSSID', 'type': 'mac_address'}
        }
    },
    12: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_NAN",
        "initial_rule": "attrs",
        "attrs": {
            # 根据C代码，subcmd 12只包含一个属性。
            # 经过查阅内核代码，QCA_WLAN_VENDOR_ATTR_NAN 的 type_id 通常是 2。
            # 我们将它定义为一个普通的、非嵌套的属性。
            2:{'name': 'QCA_WLAN_VENDOR_ATTR_NAN_DATA_BLOB', 'type': 'hex'}
        }
        # 注意：这里没有 nested_rules，因为我们不希望解析器进入这个属性的内部。
    },
    106:{   
        "name": "QCA_NL80211_VENDOR_SUBCMD_TRIGGER_SCAN",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_INVALID_PARAM', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_IE', 'type': 'hex'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_FREQUENCIES', 'type': 'u32'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_SSIDS', 'type': 'u32'},
                4: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_SUPP_RATES', 'type': 'u32'},
                5: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_TX_NO_CCK_RATE', 'type': 'u32'},
                6: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_FLAGS', 'type': 'u8'},
                7: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_COOKIE', 'type': 'u64'},
                8: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_STATUS', 'type': 'hex'},
                9: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_MAC', 'type': 'mac_address'},
                10: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_MAC_MASK', 'type': 'mac_address'},
                11: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_BSSID', 'type': 'u32'},
                12: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_DWELL_TIME', 'type': 'hex'},
                13: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_PRIORITY', 'type': 'hex'},
                14: {'name': 'QCA_WLAN_VENDOR_ATTR_SCAN_AFTER_LAST', 'type': 'hex'}
        },
        # 新增的、专门用于解释列表内容的规则集
        "frequency_list_attrs": {
            "*": { "name": "Frequency", "type": "u32" }
        },
        "ssid_list_attrs": { 
            "*": { "name": "SSID", "type": "string" } 
        }
    },
    65032: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_CHANGE_BSS",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_INVALID', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_VDEV_ID', 'type': 'u32'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_DEVICE_MODE', 'type': 'u32'},
                4: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_AP_ISOLATE', 'type': 'u32'},
                5: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_RESULT', 'type': 's32'}
        }
    },
    65036: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_DEL_STATION",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_INVALID', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_VDEV_ID', 'type': 'u32'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_DEVICE_MODE', 'type': 'u32'},
                4: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_MAC', 'type': 'mac_address'},
                5: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_RESULT', 'type': 's32'}
        }
    },
    65034: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_SCAN",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_INVALID', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_SSIDS', 'type': 'u32'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_CHANNELS', 'type': 'u32'},
                4: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_RESULT', 'type': 's32'}
        }
    },
    65037: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_GET_STATION",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_INVALID', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_VDEV_ID', 'type': 'u32'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_DEVICE_MODE', 'type': 'u32'},
                4: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_MAC', 'type': 'mac_address'},
                5: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_RESULT', 'type': 's32'}
        }
    },
    65028: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_STOP_AP",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_STOP_AP_INVALID', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_STOP_AP_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_STOP_AP_RESULT', 'type': 's32'}
        }
    },
    65029: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_CONNECT",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_INVALID', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_SSID', 'type': 'string'},
                3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_SSID_LEN', 'type': 'u32'},
                4: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_BSSID', 'type': 'mac_address'}
        }
    },
    65030: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_DISCONNECT",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DISCONNECT_INVALID', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DISCONNECT_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DISCONNECT_REASON', 'type': 'u16'}
        }
    },
    65031: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_BEACON_CHANGE",
        "initial_rule": "attrs",
        "attrs": {
                0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_BEACON_CHANGE_INVALID', 'type': 'u32'},
                1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_BEACON_CHANGE_IFNAME', 'type': 'string'},
                2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_BEACON_CHANGE_RESULT', 'type': 's32'}
        }
    },
    188: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_UPDATE_STA_INFO",
        "initial_rule": "attrs",
        "attrs": {
            0: { "name": "QCA_WLAN_VENDOR_ATTR_UPDATE_STA_INFO_INVALID", "type": "u32" },
            1: { "name": "QCA_WLAN_VENDOR_ATTR_UPDATE_STA_INFO_CONNECT_CHANNELS", "type": "s32" },
        }
    },
    189: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_DRIVER_DISCONNECT_REASON",
        "initial_rule": "attrs",
        "attrs": {
            0: { "name": "QCA_WLAN_VENDOR_ATTR_DRIVER_DISCONNECT_REASON_INVALID", "type": "u32" },
            37: { "name": "QCA_WLAN_VENDOR_ATTR_GET_STATION_INFO_DRIVER_DISCONNECT_REASON", "type": "u32" }
        }
    },
    65038: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_CACHE_STA_INFO",
        "initial_rule": "attrs",
        "attrs": {
            0:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_INVALID", "type": "u32" },
            1:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_IFNAME", "type": "string" },
            2:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_MAC", "type": "mac_address" },
            3:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_FREQ", "type": "u32" },
            4:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_RSSI", "type": "s32" },
            5:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_TX_RATE", "type": "u32" },
            6:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_RX_RATE", "type": "u32" },
            7:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_REASON", "type": "u32" },
            8:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_TX_RETRY_EXHAUST_FW", "type": "u32" },
            9:  { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_RX_FCS_COUNT", "type": "u32" },
            10: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_ASSOC_TS", "type": "u64" },
            11: { "name": "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_DISASSOC_TS", "type": "u64" }
        }
    },
    
    254: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_IDLE_SHUTDOWN",
        "initial_rule": "attrs",
        "attrs": {
            1: { "name": "QCA_WLAN_VENDOR_ATTR_IDLE_SHUTDOWN_STATUS", "type": "u32" }
        }
    },
    65040: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_DEL_VIF",
        "initial_rule": "attrs",
        "attrs": {
            0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_VIF_INVALID', 'type': 'u32'},
            1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_VIF_IFNAME', 'type': 'string'},
            2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_VIF_MAC_ADDR', 'type': 'mac_address'},
            3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_VIF_RESULT', 'type': 's32'}
        }
    },
    65039: {
    "name": "QCA_NL80211_VENDOR_SUBCMD_REG_RULES_RESP",
    "initial_rule": "top_level_attrs",

    "top_level_attrs": {
        1: { "name": "QCA_WLAN_VENDOR_ATTR_REG_COUNTRY_CODE", "type": "string" },
        2: { "name": "QCA_WLAN_VENDOR_ATTR_REG_RULES_LIST", "type": "nested" }
    },
    "channel_list_attrs": {
        "*": { "name": "", "type": "nested" }
    },
    "channel_entry_attrs": {
        4: { "name": "QCA_WLAN_VENDOR_ATTR_REG_CHANNEL_FREQ", "type": "u32"},
        5: { "name": "QCA_WLAN_VENDOR_ATTR_REG_CHANNEL_MAX_POWER", "type": "u32"},
        6: { "name": "QCA_WLAN_VENDOR_ATTR_REG_CHANNEL_FLAGS", "type": "u32"}
    },
    "nested_rules": {
        "top_level_attrs": {
            2: "channel_list_attrs"
        },
        "channel_list_attrs": {
            "*": "channel_entry_attrs"
        }
    }
},
    65041: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_ASSOC_SUCC",
        "initial_rule": "attrs",
        "attrs": {
            0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_SUCC_INVALID', 'type': 'u32'},
            1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_SUCC_IFNAME', 'type': 'string'},
            2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_SUCC_MAC_ADDR', 'type': 'mac_address'},
            3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_SUCC_FREQ', 'type': 'u32'},
            4: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_SUCC_ID', 'type': 'u32'},
            5: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_SUCC_CAPS_FLAGS', 'type': 'u32'},
            6: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_SUCC_ASSOC_REQ_IES', 'type': 'assoc_req_ies'},
        }
    },
    65042: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_ASSOC_FAIL",
        "initial_rule": "attrs",
        "attrs": {
            0: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_FAIL_INVALID', 'type': 'u32'},
            1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_FAIL_IFNAME', 'type': 'string'},
            2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_FAIL_MAC_ADDR', 'type': 'mac_address'},
            3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_FAIL_REASON', 'type': 'u32'},
            4: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_ASSOC_FAIL_REQ_IES', 'type': 'assoc_req_ies'},
        }
    },
    56:{
        "name": "QCA_NL80211_VENDOR_SUBCMD_DFS_OFFLOAD_CAC_STARTED",
        "initial_rule": "attrs",
        "attrs": {
            0: {'name': 'QCA_WLAN_VENDOR_ATTR_DFS_OFFLOAD_CAC_STARTED_INVALID', 'type': 'u32'},
            38: {'name': 'NL80211_ATTR_WIPHY_FREQ', 'type': 'u32'}
        }
    },
    57: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_DFS_OFFLOAD_CAC_FINISHED",
        "initial_rule": "attrs",
        "attrs": {
            0: {'name': 'QCA_WLAN_VENDOR_ATTR_DFS_OFFLOAD_CAC_FINISHED_INVALID', 'type': 'u32'},
            38: {'name': 'NL80211_ATTR_WIPHY_FREQ', 'type': 'u32'}
        }
    },
    
    157: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_HANG_REASON",
        "initial_rule": "attrs",
        "attrs": {
            0: {'name': 'QCA_WLAN_VENDOR_ATTR_HANG_REASON_INVALID', 'type': 'u32'},
            1: {'name': 'QCA_WLAN_VENDOR_ATTR_HANG_REASON', 'type': 'u32'},
            2: {'name': 'QCA_WLAN_VENDOR_ATTR_HANG_REASON_DATA', 'type': 'hex'}
        }
    },

    214: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_DRIVER_READY",
        "initial_rule": "attrs",
        "attrs": {
        }
    },

    51: {
    "name": "QCA_NL80211_VENDOR_SUBCMD_KEY_MGMT_ROAM_AUTH",
    "initial_rule": "attrs",
    "attrs": {
        0:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_INVALID', 'type': 'u32'},
        1:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_BSSID', 'type': 'mac'},
        2:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_REQ_IE', 'type': 'hex'},
        3:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_RESP_IE', 'type': 'hex'},
        4:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_AUTHORIZED', 'type': 'u8'},
        5:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_KEY_REPLAY_CTR', 'type': 'hex'},
        6:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_PTK_KCK', 'type': 'hex'},
        7:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_PTK_KEK', 'type': 'hex'},
        8:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_SUBNET_STATUS', 'type': 'u8'},
        9:  {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_STATUS', 'type': 'u16'},
        10: {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_RETAIN_CONNECTION', 'type': 'u8'},
        11: {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_PMK', 'type': 'hex'},
        12: {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_PMKID', 'type': 'hex'},
        13: {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_FILS_ERP_NEXT_SEQ_NUM', 'type': 'u16'},
        14: {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_REASON', 'type': 'u16'},
        15: {'name': 'QCA_WLAN_VENDOR_ATTR_ROAM_AUTH_MLO_LINKS', 'type': 'nested'}
        }
    },

    65027: {
        "name": "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_CHANGE_IFACE",
        "initial_rule": "attrs",
        "attrs": {
            1: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_IFACE_IFNAME', 'type': 'string'},
            2: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_IFACE_TYPE', 'type': 'u32'},
            3: {'name': 'QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_IFACE_RESULT', 'type': "s32" }
        }
    }
}