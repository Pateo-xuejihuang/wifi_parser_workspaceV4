// display_definitions.js

// 这个文件定义了从技术名称/值到人类可读的中文标签/文本的映射。
// 当您想要修改网页上显示的内容时，只需要编辑这个文件。

const DISPLAY_MAPPINGS = {
    "QCA_NL80211_VENDOR_SUBCMD_WLAN_MAC_INFO": {
        "friendly_name": "WLAN MAC 硬件信息",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_MAC_INFO": { "label": "MAC 信息容器" },
            "MAC_ID_CONTAINER_0": { "label": "MAC 0 " },
            "MAC_ID_CONTAINER_1": { "label": "MAC 1 " },
            "QCA_WLAN_VENDOR_ATTR_MAC_INFO_MAC_ID": { "label": "MAC ID" },
            "QCA_WLAN_VENDOR_ATTR_MAC_INFO_BAND": {
                "label": "频段能力",
                "values": {
                    "1": "2.4 GHz",
                    "2": "5 GHz",
                    "4": "6 GHz"
                }
            },
            "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO": { "label": "接口信息" },
            "INTERFACE_CONTAINER_0": { "label": "接口 0" },
            "INTERFACE_CONTAINER_1": { "label": "接口 1" },
            "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO_IFINDEX": { "label": "接口索引 (ifindex)" },
            "QCA_WLAN_VENDOR_ATTR_MAC_IFACE_INFO_FREQ": { "label": "当前频率 (MHz)" }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_START_AP": {
        "friendly_name": "启动 AP (SoftAP)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_CONTAINER": { "label": "配置容器" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_FREQ": { "label": "频率 (MHz)" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_BW": {
                "label": "带宽",
                "values": {
                    "0": "20 MHz",
                    "1": "40 MHz",
                    "2": "80 MHz",
                    "3": "160 MHz",
                    "4": "80+80 MHz",
                    "5": "5 MHz",
                    "6": "10 MHz",
                    "7": "320 MHz",
                    "8": "无效",
                    "9": "MAX (保留)"
                }
            },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_SSID": { "label": "热点名称 (SSID)" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_FLAGS": { "label": "标志位" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_RESULT": {
                "label": "启动AP结果",
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_START_AP_IFNAME": { "label": "接口名" }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_CACHE_STA_INFO": {
    "friendly_name": "终端设备断开连接 (WIFIDBG_CACHE_STA_INFO)",
    "attributes": {
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_IFNAME": { "label": "接口名" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_MAC": { "label": "终端 MAC 地址" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_FREQ": { "label": "终端频率 (MHz)" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_TX_RETRY_EXHAUST_FW": { "label": "发送重试耗尽 (TX Retry Exhausted)" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_RX_FCS_COUNT": { "label": "接收 FCS 错误计数" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_RSSI": { "label": "信号强度 (RSSI)" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_REASON": { "label": "断开原因" ,
            "values": {
                    "0": "未指定失败",
                    "1": "之前的认证已失效",
                    "2": "Deauth/Disassoc: 离开 BSS/IBSS/ESS",
                    "3": "发送端正在离开或已离开网络(如切换 AP)",
                    "4": "因 STA 长时间未通信，被 AP 认定为超时而断开",
                    "5": "AP 无足够资源(如关联表满)处理更多 STA",
                    "6": "收到未认证 STA 的 Class 2 帧（如数据帧），协议违规",
                    "7": "收到未关联 STA 的 Class 3 帧（如 QoS 数据），协议违规",
                    "8": "手机(iOS/Android)锁屏或省电时断开"
            }
        },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_TX_RATE": { "label": "原始发送速率", "display": "none" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_RX_RATE": { "label": "原始接收速率", "display": "none" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_ASSOC_TS":   { "label": "关联时间戳 (Jiffies)", "display": "none" },
        "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_DISASSOC_TS": { "label": "断开时间戳 (Jiffies)", "display": "none" },

        "COMPUTED_TX_RATE_MBPS": {
            "label": "发送速率",
            "format": "kbps_to_mbps",
            "inputs": ["QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_TX_RATE"]
        },

        "COMPUTED_RX_RATE_MBPS": {
            "label": "接收速率",
            "format": "kbps_to_mbps",
            "inputs": ["QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_RX_RATE"]
        },

        "COMPUTED_CONNECTION_DURATION": {
            "label": "首次上线持续时长",
            "format": "duration",
            "inputs": [
                "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_ASSOC_TS",
                "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CACHE_STATION_DISASSOC_TS"
            ],
            "params": { "hz": 250 }
        }
    }
},
    "QCA_NL80211_VENDOR_SUBCMD_SCAN_DONE": {
        "friendly_name": "扫描完成事件",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_SCAN_SSIDS": { "label": "SSID 列表" },
            "QCA_WLAN_VENDOR_ATTR_SCAN_FREQUENCIES": { "label": "扫描的信道列表" },
            "Frequency": { "label": "扫描频率 (MHz)" },
            "SSID": { "label": "SSID" },
            "QCA_WLAN_VENDOR_ATTR_SCAN_COOKIE": { "label": "扫描 Cookie" },
            "QCA_WLAN_VENDOR_ATTR_SCAN_STATUS": {
                "label": "扫描状态",
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_ADD_VIF": {
        "friendly_name": "添加虚拟接口 (VIF)",
        "attributes": {
            "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_CONTAINER": { "label": "配置容器" },
            "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_IFNAME": { "label": "接口名" },
            "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_IFTYPE": { 
                "label": "接口类型",
                "values": {
                    "0": "未指定",
                    "1": "Ad-Hoc 接口",
                    "2": "STA 接口",
                    "3": "AP 接口",
                    "4": "AP VLAN 接口",
                    "5": "WDS 接口",
                    "6": "监控接口",
                    "7": "Mesh Point 接口",
                    "8": "P2P Client 接口",
                    "9": "P2P GO 接口",
                    "10": "P2P Device 接口",
                    "11": "OCB 接口",
                    "12": "NAN 接口"
                }
            },
            "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_NAME_ASSIGN_TYPE": { 
                "label": "名称分配类型",
                "values": {
                    "0": "未知/默认方式",
                    "01": "内核自动枚举 (如 eth0, wlan0)",
                    "02": "可预测名称 (如基于MAC/位置)",
                    "03": "用户空间指定名称",
                    "04": "被用户空间重命名"
                }
            },
            "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_FLAGS": { "label": "标志位" },
            "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_MAC_ADDR": { "label": "MAC 地址" },
            "QCA_NL80211_VENDOR_ATTR_WIFIDBG_ADD_VIF_RESULT": { 
                "label": "添加结果",
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_INTEROP_ISSUES_AP": {
                "friendly_name": "互操作性问题 AP",
                "attributes": {
                    "QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_TYPE": { "label": "AP 类型" },
                    "QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_LIST": { "label": "AP 列表" },
                    "QCA_WLAN_VENDOR_ATTR_INTEROP_ISSUES_AP_BSSID": { "label": "AP BSSID" }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_NAN": {
        "friendly_name": "邻近感知网络 (NAN) 事件",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_NAN_DATA_BLOB": { "label": "NAN 事件原始数据" }
        }
    },
       "QCA_NL80211_VENDOR_SUBCMD_DO_ACS": {
        "friendly_name": "自动信道选择 (ACS) 结果",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_ACS_PRIMARY_FREQUENCY": { "label": "主信道频率 (MHz)" },
            "QCA_WLAN_VENDOR_ATTR_ACS_SECONDARY_FREQUENCY": { "label": "次信道频率 (MHz)" },
            "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG0_CENTER_FREQUENCY": { "label": "VHT Seg0 中心频率 (MHz)" },
            "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG1_CENTER_FREQUENCY": { "label": "VHT Seg1 中心频率 (MHz)" },
            "QCA_WLAN_VENDOR_ATTR_ACS_PRIMARY_CHANNEL": { "label": "主信道号" },
            "QCA_WLAN_VENDOR_ATTR_ACS_SECONDARY_CHANNEL": { "label": "次信道号" },
            "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG0_CENTER_CHANNEL": { "label": "VHT Seg0 中心信道号" },
            "QCA_WLAN_VENDOR_ATTR_ACS_VHT_SEG1_CENTER_CHANNEL": { "label": "VHT Seg1 中心信道号" },
            "QCA_WLAN_VENDOR_ATTR_ACS_CHWIDTH": {
                "label": "信道带宽",
                "values": {
                    "20": "20 MHz",
                    "40": "40 MHz",
                    "80": "80 MHz",
                    "160": "160 MHz",
                    "320": "320 MHz"
                }
            },
            "QCA_WLAN_VENDOR_ATTR_ACS_HW_MODE": {
                "label": "硬件模式",
                "values": {
                    "0": "802.11b",
                    "1": "802.11g (2.4GHz)",
                    "2": "802.11a (5GHz)"
                }
            },
            "QCA_WLAN_VENDOR_ATTR_ACS_HT_ENABLED": { "label": "HT (802.11n) 启用", "values": { "1": "是", "0": "否" } },
            "QCA_WLAN_VENDOR_ATTR_ACS_HT40_ENABLED": { "label": "HT40 启用", "values": { "1": "是", "0": "否" } },
            "QCA_WLAN_VENDOR_ATTR_ACS_VHT_ENABLED": { "label": "VHT (802.11ac) 启用", "values": { "1": "是", "0": "否" } },
            "QCA_WLAN_VENDOR_ATTR_ACS_PUNCTURE_BITMAP": { "label": "Puncture 位图" },
            "QCA_WLAN_VENDOR_ATTR_ACS_CH_LIST": { "label": "信道列表" },
            "QCA_WLAN_VENDOR_ATTR_ACS_FREQ_LIST": { "label": "频率列表" }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_TRIGGER_SCAN": {
        "friendly_name": "触发扫描",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_SCAN_SSIDS": { "label": "SSID 列表" },
            "QCA_WLAN_VENDOR_ATTR_SCAN_FREQUENCIES": { "label": "扫描的信道列表" },
            "Frequency": { "label": "扫描频率 (MHz)" },
            "SSID": { "label": "SSID" },
            "QCA_WLAN_VENDOR_ATTR_SCAN_COOKIE": { "label": "扫描 Cookie" },
            "QCA_WLAN_VENDOR_ATTR_SCAN_STATUS": {
                "label": "扫描状态",
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_CHANGE_BSS": {
        "friendly_name": "切换 BSS (Change BSS)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_VDEV_ID": { "label": "虚拟设备ID (vdev_id)" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_DEVICE_MODE": { "label": "设备模式" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_DEVICE_MODE": {
                "label": "设备模式",
                "values": {
                    "0": "STA模式",
                    "1": "AP模式",
                    "2": "P2P Client模式",
                    "3": "P2P GO模式",
                    "4": "FTM模式",
                    "5": "IBSS模式",
                    "6": "Monitor模式",
                    "7": "P2P Device模式",
                    "8": "OCB模式",
                    "9": "EPPING模式",
                    "10": "QVIT模式",
                    "11": "NDI模式",
                    "12": "WDS模式",
                    "13": "BTAMP模式",
                    "14": "AHDEMO模式",
                    "15": "TDLS模式",
                    "16": "NAN DISC模式"
                }
            },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_AP_ISOLATE": { "label": "AP隔离",
                "values": {
                    "0": "禁用",
                    "1": "启用"
                }
             },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CHANGE_BSS_RESULT": { "label": "切换结果",
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
             }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_DEL_STATION": {
        "friendly_name": "删除终端",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_VDEV_ID": { "label": "虚拟设备ID (vdev_id)" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_DEVICE_MODE": { "label": "设备模式",
                "values": {
                    "0": "STA模式",
                    "1": "AP模式",
                    "2": "P2P Client模式",
                    "3": "P2P GO模式",
                    "4": "FTM模式",
                    "5": "IBSS模式",
                    "6": "Monitor模式",
                    "7": "P2P Device模式",
                    "8": "OCB模式",
                    "9": "EPPING模式",
                    "10": "QVIT模式",
                    "11": "NDI模式",
                    "12": "WDS模式",
                    "13": "BTAMP模式",
                    "14": "AHDEMO模式",
                    "15": "TDLS模式",
                    "16": "NAN DISC模式"
                }
            },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_MAC": { "label": "终端MAC地址" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_STATION_RESULT": { "label": "删除结果",
                "values": {
                    "0": "成功",
                    "-2": "错误：已被驱动删除"
                }
             }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_LINK_PROPERTIES": {
        "friendly_name": "链路属性 (Link Properties)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_NSS": { "label": "空间流数 (NSS)" },
            "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_RATE_FLAGS": { "label": "速率标志 (Rate Flags)" },
            "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_FREQ": { "label": "频率 (MHz)" },
            "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_MAC_ADDR": { "label": "MAC地址" },
            "QCA_WLAN_VENDOR_ATTR_LINK_PROPERTIES_STA_FLAGS": { "label": "STA标志位" },
            "mask":{ "label": "掩码",
                "values": {
                    "1": "__NL80211_STA_FLAG_INVALID",
                    "2": "NL80211_STA_FLAG_AUTHORIZED",
                    "4": "NL80211_STA_FLAG_SHORT_PREAMBLE",
                    "8": "NL80211_STA_FLAG_WME",
                    "16": "NL80211_STA_FLAG_MFP",
                    "32": "NL80211_STA_FLAG_AUTHENTICATED",
                    "64": "NL80211_STA_FLAG_TDLS_PEER",
                    "128": "NL80211_STA_FLAG_ASSOCIATED"
                }
            },
            "set": { "label": "设置",
                "values": {
                    "0": "未设置",
                    "1": "已设置"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_SCAN": {
        "friendly_name": "调试扫描 (WIFIDBG_SCAN)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_SSIDS": { "label": "扫描 SSID 数量" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_CHANNELS": { "label": "扫描信道数量" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_SCAN_N_RESULT": { "label": "扫描结果", 
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_GET_STATION": {
        "friendly_name": "获取终端信息 (WIFIDBG_GET_STATION)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_VDEV_ID": { "label": "虚拟设备ID (vdev_id)" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_DEVICE_MODE": { "label": "设备模式",
                "values": {
                    "0": "STA模式",
                    "1": "AP模式",
                    "2": "P2P Client模式",
                    "3": "P2P GO模式",
                    "4": "FTM模式",
                    "5": "IBSS模式",
                    "6": "Monitor模式",
                    "7": "P2P Device模式",
                    "8": "OCB模式",
                    "9": "EPPING模式",
                    "10": "QVIT模式",
                    "11": "NDI模式",
                    "12": "WDS模式",
                    "13": "BTAMP模式",
                    "14": "AHDEMO模式",
                    "15": "TDLS模式",
                    "16": "NAN DISC模式"
                }
             },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_MAC": { "label": "终端MAC地址" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_GET_STATION_RESULT": { "label": "获取结果", 
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_STOP_AP": {
        "friendly_name": "停止 AP (WIFIDBG_STOP_AP)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_STOP_AP_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_STOP_AP_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_STOP_AP_RESULT": { "label": "停止结果", 
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_CONNECT": {
        "friendly_name": "连接 AP (WIFIDBG_CONNECT)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_SSID": { "label": "SSID" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_SSID_LEN": { "label": "SSID 长度" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_CONNECT_BSSID": { "label": "BSSID (MAC地址)" }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_DISCONNECT": {
        "friendly_name": "断开连接 (WIFIDBG_DISCONNECT)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DISCONNECT_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DISCONNECT_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DISCONNECT_REASON": { "label": "断开原因",
                "values": {
                    "0": "未指定失败",
                    "1": "之前的认证已失效",
                    "2": "Deauth/Disassoc: 离开 BSS/IBSS/ESS",
                    "3": "发送端正在离开或已离开网络(如切换 AP)",
                    "4": "因 STA 长时间未通信，被 AP 认定为超时而断开",
                    "5": "AP 无足够资源(如关联表满)处理更多 STA",
                    "6": "收到未认证 STA 的 Class 2 帧（如数据帧），协议违规",
                    "7": "收到未关联 STA 的 Class 3 帧（如 QoS 数据），协议违规",
                    "8": "手机(iOS/Android)锁屏或省电时断开"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_BEACON_CHANGE": {
        "friendly_name": "信标参数变更 (WIFIDBG_BEACON_CHANGE)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_BEACON_CHANGE_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_BEACON_CHANGE_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_BEACON_CHANGE_RESULT": {
                "label": "变更结果",
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_UPDATE_STA_INFO": {
        "friendly_name": "更新终端信息 (UPDATE_STA_INFO)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_UPDATE_STA_INFO_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_UPDATE_STA_INFO_CONNECT_CHANNELS": { "label": "连接信道" }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_DRIVER_DISCONNECT_REASON": {
        "friendly_name": "驱动断开原因 (DRIVER_DISCONNECT_REASON)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_DRIVER_DISCONNECT_REASON_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_GET_STATION_INFO_DRIVER_DISCONNECT_REASON": { "label": "驱动断开原因码",
                "values": {
                    "0": "未指定（手动断开或IEEE标准原因码通常显示为UNSPECIFIED，这是驱动的正常设计行为）",
                    "1": "内部漫游失败",
                    "2": "外部漫游失败",
                    "3": "网关不可达",
                    "4": "不支持的信道CSA",
                    "5": "运营信道因室内限制被禁用",
                    "6": "运营信道被用户禁用",
                    "7": "设备恢复",
                    "8": "密钥超时",
                    "9": "运营信道频段切换",
                    "10": "接口Down",
                    "11": "对端重试失败",
                    "12": "对端不活跃",
                    "13": "SA Query超时",
                    "14": "Beacon丢失失败",
                    "15": "信道切换失败",
                    "16": "用户主动断开"
                }
             }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_WIFIDBG_DEL_VIF": {
        "friendly_name": "删除虚拟接口 (WIFIDBG_DEL_VIF)",
        "attributes": {
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_VIF_INVALID": { "label": "无效参数" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_VIF_IFNAME": { "label": "接口名" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_VIF_MAC_ADDR": { "label": "MAC地址" },
            "QCA_WLAN_VENDOR_ATTR_WIFIDBG_DEL_VIF_RESULT": {
                "label": "删除结果",
                "values": {
                    "0": "成功",
                    "1": "失败"
                }
            }
        }
    },
    "QCA_NL80211_VENDOR_SUBCMD_REG_RULES_RESP": {
    "friendly_name": "国家码设置 (REG_RULES_RESP)",
    "attributes": {
        "QCA_WLAN_VENDOR_ATTR_REG_COUNTRY_CODE": { "label": "国家码" },
        "QCA_WLAN_VENDOR_ATTR_REG_RULES_LIST": { "label": "信道规则列表", "is_list": true },
        "QCA_WLAN_VENDOR_ATTR_REG_CHANNEL_FREQ": { "label": "频率 (MHz)",
            "values": {
                "2412": "信道 1 (2412 MHz)",
                "2417": "信道 2 (2417 MHz)",
                "2422": "信道 3 (2422 MHz)",
                "2427": "信道 4 (2427 MHz)",
                "2432": "信道 5 (2432 MHz)",
                "2437": "信道 6 (2437 MHz)",
                "2442": "信道 7 (2442 MHz)",
                "2447": "信道 8 (2447 MHz)",
                "2452": "信道 9 (2452 MHz)",
                "2457": "信道 10 (2457 MHz)",
                "2462": "信道 11 (2462 MHz)",
                "2467": "信道 12 (2467 MHz)",
                "2472": "信道 13 (2472 MHz)",
                "2484": "信道 14 (2484 MHz)",
                "5180": "信道 36 (5180 MHz)",
                "5200": "信道 40 (5200 MHz)",
                "5220": "信道 44 (5220 MHz)",
                "5240": "信道 48 (5240 MHz)",
                "5260": "信道 52 (5260 MHz)",
                "5280": "信道 56 (5280 MHz)",
                "5300": "信道 60 (5300 MHz)",
                "5320": "信道 64 (5320 MHz)",
                "5500": "信道 100 (5500 MHz)",
                "5520": "信道 104 (5520 MHz)",
                "5540": "信道 108 (5540 MHz)",
                "5560": "信道 112 (5560 MHz)",
                "5580": "信道 116 (5580 MHz)",
                "5600": "信道 120 (5600 MHz)",
                "5620": "信道 124 (5620 MHz)",
                "5640": "信道 128 (5640 MHz)",
                "5660": "信道 132 (5660 MHz)",
                "5680": "信道 136 (5680 MHz)",
                "5700": "信道 140 (5700 MHz)",
                "5720": "信道 144 (5720 MHz)",               
                "5745": "信道 149 (5745 MHz)",
                "5765": "信道 153 (5765 MHz)",
                "5785": "信道 157 (5785 MHz)",
                "5805": "信道 161 (5805 MHz)",
                "5825": "信道 165 (5825 MHz)",
                "5925": "信道 169 (5925 MHz)",
                "5945": "信道 173 (5945 MHz)",
                "5965": "信道 177 (5965 MHz)",
                "5985": "信道 181 (5985 MHz)",
                "6005": "信道 185 (6005 MHz)"
         }},
        "QCA_WLAN_VENDOR_ATTR_REG_CHANNEL_MAX_POWER": { "label": "最大功率 (dBm)" },
        "QCA_WLAN_VENDOR_ATTR_REG_CHANNEL_FLAGS": { "label": "原始标志位",
            "values": {
                "524288": "有效信道 (无特殊限制)",
                "524296": "DFS",
                "524304": "NO_IR (被动扫描)",
                "524312": "DFS + NO_IR (被动扫描)",
                "524320": "带宽限制: 禁止HT40向下扩展 (NO_HT40MINUS)",
                "524328": "DFS + 带宽限制: 禁止HT40向下扩展 (NO_HT40MINUS)",
                "524544": "带宽限制: 禁止HT40向上扩展 (NO_HT40PLUS)",
                "524560": "NO_IR + 带宽限制: 禁止HT40向上扩展 (NO_HT40PLUS)",
                "524576": "带宽限制: 禁止HT40双向扩展 (NO_HT40PLUS/MINUS)",
                "524672": "带宽限制: 禁止80MHz + 禁止HT40向上扩展 (NO_80MHZ + NO_HT40PLUS)",
                "524688": "NO_IR + 带宽限制: 禁止80MHz + 禁止HT40向上扩展 (NO_80MHZ + NO_HT40PLUS)",
                "524704": "带宽限制: 禁止80MHz + 禁止HT40双向扩展 (NO_80MHZ + NO_HT40PLUS/MINUS)",
                "524802": "INDOOR_ONLY + AP模式特殊限制 (TPC（发射功率控制）+强制的DFS)",
                "524810": "INDOOR_ONLY + DFS + AP模式特殊限制 (TPC（发射功率控制）+强制的DFS)",
                "524826": "INDOOR_ONLY + DFS + NO_IR + AP模式特殊限制 (TPC（发射功率控制）+强制的DFS)",
                "524834": "INDOOR_ONLY + AP模式特殊限制 (TPC（发射功率控制）+强制的DFS) + 带宽限制 (NO_HT40MINUS)"
         }}
        }
    }
}
