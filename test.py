import os
from pprint import pprint

import ipdb
from netbane.plugins.inventory.netbox import netbox_transform
from nornir import InitNornir
from nornir.core.inventory import Host
from nornir.core.plugins.inventory import TransformFunctionRegister
from nornir.core.task import Result, Task
from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command
from nornir_utils.plugins.functions import print_result

TransformFunctionRegister.register("netbox_transform", netbox_transform)

os.environ[
    "NET_TEXTFSM"
] = "/usr/local/lib/python3.9/site-packages/ntc_templates/templates"

nr = InitNornir(config_file="config.yaml")
host = nr.filter(name="SWTC21AC02")


def get_config_and_facts(task: Task):
    task.run(
        name="get config",
        task=netmiko_send_command,
        command_string="show running-config",
    )
    task.run(
        name="get CDP neighbors",
        task=netmiko_send_command,
        command_string="show cdp neighbors detail",
        use_textfsm=True,
    )
    task.run(
        name="get facts",
        task=netmiko_send_command,
        command_string="show version",
        use_textfsm=True,
    )


def get_wlc_ap_list(task: Task):
    task.host.open_connection(
        "netmiko", platform="cisco_wlc_ssh", configuration=task.nornir.config
    )
    task.run(
        task=netmiko_send_command, command_string="show ap summary", use_textfsm=True
    )
    task.host.close_connection("netmiko")


wlc = nr.filter(name="WWTC19WC11")
result = wlc.run(task=get_wlc_ap_list)
print_result(result)

ipdb.set_trace()
