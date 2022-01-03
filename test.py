from pprint import pprint

import ipdb
from nornir import InitNornir
from nornir.core.inventory import Host
from nornir_napalm.plugins.tasks.napalm_get import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir.core.plugins.inventory import TransformFunctionRegister


def netbox_transform(host: Host) -> None:
    # store raw netbox data in separate key in case we want it later
    host.data["netbox"] = host.data
    netbox = host.data["netbox"]
    host.data["site"] = netbox["site"]["slug"].lower()


TransformFunctionRegister.register("netbox_transform", netbox_transform)

nr = InitNornir(config_file="config.yaml")
host = nr.filter(name='SWTC21AC02')

result = host.run(task=napalm_get, getters=['facts'])
print_result(result)

ipdb.set_trace()
