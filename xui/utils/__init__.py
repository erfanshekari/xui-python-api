import uuid
from random import randint
from string import ascii_lowercase, ascii_uppercase

def generate_password(length: int = 10) -> str:
    response = ""
    for _ in range(length):
        if randint(0,1):
            source = ascii_lowercase
            if randint(0,1):
                source = ascii_uppercase
            response += source[randint(0, (len(source) - 1))]
            continue
        response += str(randint(0, 9))
    return response

def generate_default_settings(protocol: str) -> dict:
    protocol = protocol.lower()
    if protocol == 'vmess':
        return {
                "clients": [
                    {
                    "id": str(uuid.uuid4()),
                    "alterId": 0,
                    "email": "",
                    "limitIp": 0,
                    "totalGB": 0,
                    "expiryTime": ""
                    }
                ],
                "disableInsecureEncryption": False
            }
    if protocol == 'vless':
        return {
            "clients": [
                {
                "id": str(uuid.uuid4()),
                "flow": "xtls-rprx-direct",
                "email": "",
                "limitIp": 0,
                "totalGB": 0,
                "expiryTime": ""
                }
            ],
            "decryption": "none",
            "fallbacks": []
        }
    if protocol == 'shadowsocks':
        return {
            "method": "aes-256-gcm",
            "password": generate_password(),
            "network": "tcp,udp"
        }
    
    if protocol == 'dokodemo-door':
        return {
                "network": "tcp,udp"
            }
    
    if protocol == 'socks':
        return {
                "auth": "password",
                "accounts": [
                    {
                    "user": generate_password(),
                    "pass": generate_password()
                    }
                ],
                "udp": False,
                "ip": "127.0.0.1"
            }

    if protocol == 'http':
        return {
                "accounts": [
                    {
                    "user": generate_password(),
                    "pass": generate_password()
                    }
                ]
            }

def generate_default_stream_settings(protocol: str) -> dict:
    protocol = protocol.lower()
    if protocol == 'vmess' or protocol == 'vless':
        return {
                "network": "tcp",
                "security": "none",
                "tcpSettings": {
                    "acceptProxyProtocol": False,
                    "header": {
                    "type": "none"
                    }
                }
            }
    if protocol == 'trojan':
        return {
            "network": "tcp",
            "security": "tls",
            "tlsSettings": {
                "serverName": "",
                "certificates": [
                {
                    "certificateFile": "",
                    "keyFile": ""
                }
                ],
                "alpn": []
            },
            "tcpSettings": {
                "acceptProxyProtocol": False,
                "header": {
                    "type": "none"
                }
            }
        }
    
    return {
            "network": "tcp",
            "security": "none",
            "tcpSettings": {
                "acceptProxyProtocol": False,
                "header": {
                    "type": "none"
                }
            }
        }

def generate_default_sniffing(protocol: str) -> dict:
    protocol = protocol.lower()
    if protocol == 'http': return dict()
    return {
            "enabled": True,
            "destOverride": [
                "http",
                "tls"
            ]
        }