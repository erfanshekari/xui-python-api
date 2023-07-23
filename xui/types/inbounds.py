from typing import TypedDict, List

class ClientStats(TypedDict):
    id: int
    inboundId: int
    enable: bool
    email: str
    up: int
    down: int
    expiryTime: int
    total: int

class Inbound(TypedDict):
    id: int
    up: int
    down: int
    total: int
    remark: str
    enable: bool
    expiryTime: int
    listen: str
    port: int
    protocol: str
    settings: str
    streamSettings: str
    tag: str
    sniffing: str
    clientStats: List[ClientStats]
