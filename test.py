import os
from pprint import pprint

import ipdb
from netbane.plugins.inventory.netbox import netbox_transform
from nornir import InitNornir
from nornir.core.inventory import Host
from nornir.core.plugins.inventory import TransformFunctionRegister
from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command
from nornir_utils.plugins.functions import print_result

TransformFunctionRegister.register("netbox_transform", netbox_transform)

os.environ[
    "NET_TEXTFSM"
] = "/usr/local/lib/python3.9/site-packages/ntc_templates/templates"

nr = InitNornir(config_file="config.yaml")
host = nr.filter(name="SWTC21AC02")

result = host.run(
    task=netmiko_send_command,
    command_string="show cdp neighbors detail",
    use_textfsm=True,
)
print_result(result)

ipdb.set_trace()
