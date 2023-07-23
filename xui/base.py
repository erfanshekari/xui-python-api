import requests, random, json
from requests import Session
from .types import (
    XUICredentials
)
from .types.response import (
    ServerStatusResponse,
    InboundsListResponse,
    BaseXUIResponse,
    Inbound
)
from .exceptions import (
    AuthenticationFailed
)
from .utils.inbound import fill_empity_fields

class XUIBase:
    BASE_URL:str
    CREDENTIALS: XUICredentials
    session: Session

    def __init__(self, url:str, username:str, password: str) -> None:
        assert url and username and password
        if url[len(url) - 1] == '/':
            url = url[:len(url) - 1]
        self.BASE_URL = url
        self.CREDENTIALS = {
            'username': username,
            'password': password
        }

    def is_authenticated(self) -> bool: return bool(getattr(self, 'session', None))

    def authenticate(self) -> None:
        req = requests.Session()
        response = req.post(
            f'{self.BASE_URL}/login', 
            data={
                'username': self.CREDENTIALS['username'],
                'password': self.CREDENTIALS['password']
                }
        )
        if response.status_code == 200:
            json_response = response.json()
            if type(json_response) is dict:
                success = json_response.get('success')
                if success:
                    self.session = req
                    return
        raise AuthenticationFailed()

    def get_session(self) -> Session:
        if not self.is_authenticated():
            self.authenticate()
        return self.session
    
    def get_server_status(self) -> ServerStatusResponse:
        response = self.get_session().post(f'{self.BASE_URL}/server/status')
        if response.status_code == 200:
            return response.json()

    def get_all_inbounds(self) -> InboundsListResponse:
        response = self.get_session().post(f'{self.BASE_URL}/xui/inbound/list')
        if response.status_code == 200:
            return response.json()

    def delete_inbound(self, inbound_id: int) -> bool:
        assert inbound_id
        response = self.get_session().post(f'{self.BASE_URL}/xui/inbound/del/{inbound_id}')
        if response.status_code == 200:
            json_response = response.json()
            if type(json_response) is dict:
                return json_response['success']
        return False

    def create_inbound(self,
        protocol: str,
        port: int = random.randint(1000, 65000),
        listen: str = "",
        enable: bool = True,
        remark: str = "",
        settings: dict = None,
        streamSettings: dict = None,
        sniffing: dict = None

    ) -> BaseXUIResponse:
        
        payload = {
            'protocol': protocol,
            'port': port,
            'listen': listen ,
            'enable': enable,
            'remark': remark,
            'settings': settings,
            'streamSettings': streamSettings,
            'sniffing': sniffing
        }

        fill_empity_fields(payload)

        payload['settings'] = json.dumps(payload['settings'])
        payload['streamSettings'] = json.dumps(payload['streamSettings'])
        payload['sniffing'] = json.dumps(payload['sniffing'])

        response = self.get_session().post(
            f'{self.BASE_URL}/xui/inbound/add', 
            data=payload,
        )
        if response.status_code == 200:
            return response.json()
        
    def get_inbound_by_id(self, inbound_id: int) -> Inbound:
        assert inbound_id
        inbounds = self.get_all_inbounds()['obj']
        for inbound in inbounds:
            if inbound['id'] == inbound_id:
                return inbound

    def edit_inbound(self, inbound_id: int, **kwargs:Inbound) -> BaseXUIResponse:
        assert inbound_id
        inbound = self.get_inbound_by_id(inbound_id)
        assert inbound
        REQUIRED_KEYS = [
            'up',
            'down',
            'total',
            'enable',
            'remark',
            'expiryTime',
            'listen',
            'port',
            'protocol',
            'settings',
            'streamSettings',
            'sniffing'
        ]

        payload = dict()

        for key in REQUIRED_KEYS:
            value = kwargs.get(key, None)
            if value is None:
                value = inbound.get(key, None)
            
            if value is not None:
                payload[key] = value

        response = self.get_session().post(
            f'{self.BASE_URL}/xui/inbound/update/{inbound_id}',
            data=payload
        )

        if response.status_code == 200:
            return response.json()
        
    