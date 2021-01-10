#!/usr/bin/python3

import os
import sys
import requests
import json
import socket

api_base = "https://api.hetzner.cloud/v1"


def get_server_fqdn():
    return socket.getfqdn()


def get_server_hostname():
    return socket.gethostname()


def get_server_id():
    url = api_base + "/servers"
    r = requests.get(url=url, data={}, headers=headers)

    if not r.ok:
        print("Error while contacting api: %s" % (r.reason))
        print(r.text)
        sys.exit(1)

    servers = json.loads(r.text)["servers"]

    conditions = [get_server_hostname(), get_server_fqdn()]

    for server in servers:
        if server["name"] in conditions:
            return server["id"]


def assign_floating_ip(floating_ip_id):
    url = api_base + "/floating_ips/" + floating_ip_id + "/actions/assign"
    payload = json.dumps({"server": get_server_id()})
    r = requests.post(url=url, data=payload, headers=headers)

    if not r.ok:
        print("Error while contacting api: %s" % (r.reason))
        print(r.text)
        sys.exit(1)

    return True


def main(floating_ip_id):
    print("Trying to assign floating ip %s to this server." % (floating_ip_id))
    if assign_floating_ip(floating_ip_id=floating_ip_id):
        print("Successful")
        sys.exit(0)
    else:
        print("Error during floating ip assignment")
        sys.exit(1)


if __name__ == "__main__":
    if "HC_TOKEN" not in os.environ:
        print(
            "No api token found in environment variables. Use 'export HC_TOKEN=xyz' to fix the problem."
        )
        sys.exit()

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ["HC_TOKEN"],
    }

    main(floating_ip_id=sys.argv[1])
