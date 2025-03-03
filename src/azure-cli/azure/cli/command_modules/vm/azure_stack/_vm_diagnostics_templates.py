# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# flake8: noqa
# noqa
# pylint: skip-file


def get_default_diag_config(is_windows):
    if is_windows:
        return {
            "WadCfg": {
                "DiagnosticMonitorConfiguration": {
                    "overallQuotaInMB": 4096,
                    "DiagnosticInfrastructureLogs": {
                        "scheduledTransferLogLevelFilter": "Error",
                        "scheduledTransferPeriod": "PT1M"
                    },
                    "WindowsEventLog": {
                        "scheduledTransferPeriod": "PT1M",
                        "DataSource": [
                            {"name": "Application!*[System[(Level=1 or Level=2)]]"},
                            {"name": "System!*[System[(Level=1 or Level=2)]]"}
                        ]
                    },
                    "Directories": {
                        "scheduledTransferPeriod": "PT1M"
                    },
                    "PerformanceCounters": {
                        "scheduledTransferPeriod": "PT1M",
                        "PerformanceCounterConfiguration": [
                            {
                                "counterSpecifier": "\\Processor(_Total)\\% Processor Time",
                                "sampleRate": "PT15S",
                                "unit": "Percent",
                                "annotation": [
                                    {
                                        "displayName": "CPU utilization",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Processor(_Total)\\% Privileged Time",
                                "sampleRate": "PT15S",
                                "unit": "Percent",
                                "annotation": [
                                    {
                                        "displayName": "CPU privileged time",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Processor(_Total)\\% User Time",
                                "sampleRate": "PT15S",
                                "unit": "Percent",
                                "annotation": [
                                    {
                                        "displayName": "CPU user time",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Processor Information(_Total)\\Processor Frequency",
                                "sampleRate": "PT15S",
                                "unit": "Count",
                                "annotation": [
                                    {
                                        "displayName": "CPU frequency",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\System\\Processes",
                                "sampleRate": "PT15S",
                                "unit": "Count",
                                "annotation": [
                                    {
                                        "displayName": "Processes",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Process(_Total)\\Thread Count",
                                "sampleRate": "PT15S",
                                "unit": "Count",
                                "annotation": [
                                    {
                                        "displayName": "Threads",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Process(_Total)\\Handle Count",
                                "sampleRate": "PT15S",
                                "unit": "Count",
                                "annotation": [
                                    {
                                        "displayName": "Handles",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Memory\\% Committed Bytes In Use",
                                "sampleRate": "PT15S",
                                "unit": "Percent",
                                "annotation": [
                                    {
                                        "displayName": "Memory usage",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Memory\\Available Bytes",
                                "sampleRate": "PT15S",
                                "unit": "Bytes",
                                "annotation": [
                                    {
                                        "displayName": "Memory available",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Memory\\Committed Bytes",
                                "sampleRate": "PT15S",
                                "unit": "Bytes",
                                "annotation": [
                                    {
                                        "displayName": "Memory committed",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\Memory\\Commit Limit",
                                "sampleRate": "PT15S",
                                "unit": "Bytes",
                                "annotation": [
                                    {
                                        "displayName": "Memory commit limit",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\% Disk Time",
                                "sampleRate": "PT15S",
                                "unit": "Percent",
                                "annotation": [
                                    {
                                        "displayName": "Disk active time",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\% Disk Read Time",
                                "sampleRate": "PT15S",
                                "unit": "Percent",
                                "annotation": [
                                    {
                                        "displayName": "Disk active read time",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\% Disk Write Time",
                                "sampleRate": "PT15S",
                                "unit": "Percent",
                                "annotation": [
                                    {
                                        "displayName": "Disk active write time",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\Disk Transfers/sec",
                                "sampleRate": "PT15S",
                                "unit": "CountPerSecond",
                                "annotation": [
                                    {
                                        "displayName": "Disk operations",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\Disk Reads/sec",
                                "sampleRate": "PT15S",
                                "unit": "CountPerSecond",
                                "annotation": [
                                    {
                                        "displayName": "Disk read operations",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\Disk Writes/sec",
                                "sampleRate": "PT15S",
                                "unit": "CountPerSecond",
                                "annotation": [
                                    {
                                        "displayName": "Disk write operations",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\Disk Bytes/sec",
                                "sampleRate": "PT15S",
                                "unit": "BytesPerSecond",
                                "annotation": [
                                    {
                                        "displayName": "Disk speed",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\Disk Read Bytes/sec",
                                "sampleRate": "PT15S",
                                "unit": "BytesPerSecond",
                                "annotation": [
                                    {
                                        "displayName": "Disk read speed",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\PhysicalDisk(_Total)\\Disk Write Bytes/sec",
                                "sampleRate": "PT15S",
                                "unit": "BytesPerSecond",
                                "annotation": [
                                    {
                                        "displayName": "Disk write speed",
                                        "locale": "en-us"
                                    }
                                ]
                            },
                            {
                                "counterSpecifier": "\\LogicalDisk(_Total)\\% Free Space",
                                "sampleRate": "PT15S",
                                "unit": "Percent",
                                "annotation": [
                                    {
                                        "displayName": "Disk free space (percentage)",
                                        "locale": "en-us"
                                    }
                                ]
                            }
                        ]
                    },
                    "Metrics": {
                        "resourceId": "__VM_OR_VMSS_RESOURCE_ID__",
                        "MetricAggregation": [
                            {
                                "scheduledTransferPeriod": "PT1H"
                            },
                            {
                                "scheduledTransferPeriod": "PT1M"
                            }
                        ]
                    }
                }
            },
            "StorageAccount": "__DIAGNOSTIC_STORAGE_ACCOUNT__"
        }
    else:
        return {
            "StorageAccount": "__DIAGNOSTIC_STORAGE_ACCOUNT__",
            "ladCfg": {
                "diagnosticMonitorConfiguration": {
                    "eventVolume": "Medium",
                    "metrics": {
                        "metricAggregation": [
                            {
                                "scheduledTransferPeriod": "PT1H"
                            },
                            {
                                "scheduledTransferPeriod": "PT1M"
                            }
                        ],
                        "resourceId": "__VM_OR_VMSS_RESOURCE_ID__"
                    },
                    "performanceCounters": {
                        "performanceCounterConfiguration": [
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk read guest OS",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "readbytespersecond",
                                "counterSpecifier": "/builtin/disk/readbytespersecond",
                                "type": "builtin",
                                "unit": "BytesPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk writes",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "writespersecond",
                                "counterSpecifier": "/builtin/disk/writespersecond",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk transfer time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "averagetransfertime",
                                "counterSpecifier": "/builtin/disk/averagetransfertime",
                                "type": "builtin",
                                "unit": "Seconds"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk transfers",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "transferspersecond",
                                "counterSpecifier": "/builtin/disk/transferspersecond",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk write guest OS",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "writebytespersecond",
                                "counterSpecifier": "/builtin/disk/writebytespersecond",
                                "type": "builtin",
                                "unit": "BytesPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk read time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "averagereadtime",
                                "counterSpecifier": "/builtin/disk/averagereadtime",
                                "type": "builtin",
                                "unit": "Seconds"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk write time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "averagewritetime",
                                "counterSpecifier": "/builtin/disk/averagewritetime",
                                "type": "builtin",
                                "unit": "Seconds"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk total bytes",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "bytespersecond",
                                "counterSpecifier": "/builtin/disk/bytespersecond",
                                "type": "builtin",
                                "unit": "BytesPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk reads",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "readspersecond",
                                "counterSpecifier": "/builtin/disk/readspersecond",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Disk queue length",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "disk",
                                "condition": "IsAggregate=TRUE",
                                "counter": "averagediskqueuelength",
                                "counterSpecifier": "/builtin/disk/averagediskqueuelength",
                                "type": "builtin",
                                "unit": "Count"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Network in guest OS",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "network",
                                "counter": "bytesreceived",
                                "counterSpecifier": "/builtin/network/bytesreceived",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Network total bytes",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "network",
                                "counter": "bytestotal",
                                "counterSpecifier": "/builtin/network/bytestotal",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Network out guest OS",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "network",
                                "counter": "bytestransmitted",
                                "counterSpecifier": "/builtin/network/bytestransmitted",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Network collisions",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "network",
                                "counter": "totalcollisions",
                                "counterSpecifier": "/builtin/network/totalcollisions",
                                "type": "builtin",
                                "unit": "Count"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Packets received errors",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "network",
                                "counter": "totalrxerrors",
                                "counterSpecifier": "/builtin/network/totalrxerrors",
                                "type": "builtin",
                                "unit": "Count"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Packets sent",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "network",
                                "counter": "packetstransmitted",
                                "counterSpecifier": "/builtin/network/packetstransmitted",
                                "type": "builtin",
                                "unit": "Count"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Packets received",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "network",
                                "counter": "packetsreceived",
                                "counterSpecifier": "/builtin/network/packetsreceived",
                                "type": "builtin",
                                "unit": "Count"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Packets sent errors",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "network",
                                "counter": "totaltxerrors",
                                "counterSpecifier": "/builtin/network/totaltxerrors",
                                "type": "builtin",
                                "unit": "Count"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem transfers/sec",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "transferspersecond",
                                "counterSpecifier": "/builtin/filesystem/transferspersecond",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem % free space",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentfreespace",
                                "counterSpecifier": "/builtin/filesystem/percentfreespace",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem % used space",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentusedspace",
                                "counterSpecifier": "/builtin/filesystem/percentusedspace",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem used space",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "usedspace",
                                "counterSpecifier": "/builtin/filesystem/usedspace",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem read bytes/sec",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "bytesreadpersecond",
                                "counterSpecifier": "/builtin/filesystem/bytesreadpersecond",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem free space",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "freespace",
                                "counterSpecifier": "/builtin/filesystem/freespace",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem % free inodes",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentfreeinodes",
                                "counterSpecifier": "/builtin/filesystem/percentfreeinodes",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem bytes/sec",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "bytespersecond",
                                "counterSpecifier": "/builtin/filesystem/bytespersecond",
                                "type": "builtin",
                                "unit": "BytesPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem reads/sec",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "readspersecond",
                                "counterSpecifier": "/builtin/filesystem/readspersecond",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem write bytes/sec",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "byteswrittenpersecond",
                                "counterSpecifier": "/builtin/filesystem/byteswrittenpersecond",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem writes/sec",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "writespersecond",
                                "counterSpecifier": "/builtin/filesystem/writespersecond",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Filesystem % used inodes",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "filesystem",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentusedinodes",
                                "counterSpecifier": "/builtin/filesystem/percentusedinodes",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "CPU IO wait time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "processor",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentiowaittime",
                                "counterSpecifier": "/builtin/processor/percentiowaittime",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "CPU user time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "processor",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentusertime",
                                "counterSpecifier": "/builtin/processor/percentusertime",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "CPU nice time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "processor",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentnicetime",
                                "counterSpecifier": "/builtin/processor/percentnicetime",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "CPU percentage guest OS",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "processor",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentprocessortime",
                                "counterSpecifier": "/builtin/processor/percentprocessortime",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "CPU interrupt time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "processor",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentinterrupttime",
                                "counterSpecifier": "/builtin/processor/percentinterrupttime",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "CPU idle time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "processor",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentidletime",
                                "counterSpecifier": "/builtin/processor/percentidletime",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "CPU privileged time",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "processor",
                                "condition": "IsAggregate=TRUE",
                                "counter": "percentprivilegedtime",
                                "counterSpecifier": "/builtin/processor/percentprivilegedtime",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Memory available",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "availablememory",
                                "counterSpecifier": "/builtin/memory/availablememory",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Swap percent used",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "percentusedswap",
                                "counterSpecifier": "/builtin/memory/percentusedswap",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Memory used",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "usedmemory",
                                "counterSpecifier": "/builtin/memory/usedmemory",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Page reads",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "pagesreadpersec",
                                "counterSpecifier": "/builtin/memory/pagesreadpersec",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Swap available",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "availableswap",
                                "counterSpecifier": "/builtin/memory/availableswap",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Swap percent available",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "percentavailableswap",
                                "counterSpecifier": "/builtin/memory/percentavailableswap",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Mem. percent available",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "percentavailablememory",
                                "counterSpecifier": "/builtin/memory/percentavailablememory",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Pages",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "pagespersec",
                                "counterSpecifier": "/builtin/memory/pagespersec",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Swap used",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "usedswap",
                                "counterSpecifier": "/builtin/memory/usedswap",
                                "type": "builtin",
                                "unit": "Bytes"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Memory percentage",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "percentusedmemory",
                                "counterSpecifier": "/builtin/memory/percentusedmemory",
                                "type": "builtin",
                                "unit": "Percent"
                            },
                            {
                                "annotation": [
                                    {
                                        "displayName": "Page writes",
                                        "locale": "en-us"
                                    }
                                ],
                                "class": "memory",
                                "counter": "pageswrittenpersec",
                                "counterSpecifier": "/builtin/memory/pageswrittenpersec",
                                "type": "builtin",
                                "unit": "CountPerSecond"
                            }
                        ]
                    },
                    "syslogEvents": {
                        "syslogEventConfiguration": {
                            "LOG_AUTH": "LOG_DEBUG",
                            "LOG_AUTHPRIV": "LOG_DEBUG",
                            "LOG_CRON": "LOG_DEBUG",
                            "LOG_DAEMON": "LOG_DEBUG",
                            "LOG_FTP": "LOG_DEBUG",
                            "LOG_KERN": "LOG_DEBUG",
                            "LOG_LOCAL0": "LOG_DEBUG",
                            "LOG_LOCAL1": "LOG_DEBUG",
                            "LOG_LOCAL2": "LOG_DEBUG",
                            "LOG_LOCAL3": "LOG_DEBUG",
                            "LOG_LOCAL4": "LOG_DEBUG",
                            "LOG_LOCAL5": "LOG_DEBUG",
                            "LOG_LOCAL6": "LOG_DEBUG",
                            "LOG_LOCAL7": "LOG_DEBUG",
                            "LOG_LPR": "LOG_DEBUG",
                            "LOG_MAIL": "LOG_DEBUG",
                            "LOG_NEWS": "LOG_DEBUG",
                            "LOG_SYSLOG": "LOG_DEBUG",
                            "LOG_USER": "LOG_DEBUG",
                            "LOG_UUCP": "LOG_DEBUG"
                        }
                    }
                },
                "sampleRateInSeconds": 15
            }
        }
