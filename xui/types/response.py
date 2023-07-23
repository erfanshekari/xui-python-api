from typing import TypedDict, Any, List
from xui.types.inbounds import Inbound


class BaseXUIResponse(TypedDict):
    success: bool
    msg: str
    obj: Any

class _ServerStatusResponse(BaseXUIResponse):
    cpu: float
    mem: TypedDict(
        'MemoryStatus',
        {
            'current': int,
            'total': int
        }
    )
    swap: TypedDict(
        'SwapStatus',
        {
            'current': int,
            'total': int
        }
    )
    disk: TypedDict(
        'DiskStatus',
        {
            'current': int,
            'total': int
        }
    )
    xray: TypedDict(
        'DiskStatus',
        {
            "state": str,
            "errorMsg": str,
            "version": str
        }
    )
    uptime: int
    loads: List[float]
    tcpCount: int
    udpCount: int
    netIO: TypedDict(
        'NetIOStatus',
        {
            "up": int,
            "down": int,
        }
    )
    netTraffic: TypedDict(
        'NetIOStatus',
        {
            "sent": int,
            "recv": int,
        }
    )


class ServerStatusResponse(BaseXUIResponse):
    obj: _ServerStatusResponse


class InboundsListResponse(BaseXUIResponse):
    obj: List[Inbound]


