from nornir.core.plugins.inventory import TransformFunctionRegister
from nornir import InitNornir
from pprint import pprint
import ipdb



def netbox_transform(host):
    # store raw netbox data in separate key in case we want it later
    host.data['netbox'] = host.data
    netbox = host.data['netbox']

    host.data['site'] = netbox['site']['slug']


TransformFunctionRegister.register('netbox_transform', netbox_transform)

nr = InitNornir(config_file='config.yaml')

ipdb.set_trace()
