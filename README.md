# XUI Panel Python API

### Example:
~~~python
from xui import XUI

xui = XUI(
    'http://127.0.0.1:7000',
    user='admin',
    password='password'
)

status = xui.get_server_status()
~~~

### Features:
~~~python
class XUI:
    def get_server_status(): ...

    def get_all_inbounds(): ...

    def get_inbound_by_id(...): ...

    def create_inbound(...): ...

    def edit_inbound(...): ...

    def delete_inbound(...): ...
~~~
