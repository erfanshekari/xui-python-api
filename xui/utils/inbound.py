from xui.utils import (
    generate_default_settings,
    generate_default_stream_settings,
    generate_default_sniffing
)

def fill_empity_fields(inbound: dict):
    assert type(inbound) is dict
    protocol = inbound.get('protocol')

    if not inbound.get('settings', None):
        inbound['settings'] = generate_default_settings(protocol)

    if not inbound.get('streamSettings', None):
        inbound['streamSettings'] = generate_default_stream_settings(protocol)

    if not inbound.get('sniffing', None):
        inbound['sniffing'] = generate_default_sniffing(protocol)
    