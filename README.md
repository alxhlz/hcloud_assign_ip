# hcloud assign ip

This little script helps you to assign a floating ip to your current system.
It can be a useful helper in failover scenarios.

## How it woks
The script determines the hostname and fqdn of your current system and reads the servers from the hcloud api.
As soon as a match is found it does the assignment of the floating ip.

## Installation

1. git clone https://github.com/lehuizi/hcloud_assign_ip.git
2. chmod +x assign-ip.py
3. mv assign-ip.py /usr/local/bin/assign-ip

## Usage

`assign-ip <floating-ip-id>`
