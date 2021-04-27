# Devolo MagicLAN 2 API interface

This package provides a Python class for interacting with a Devolo MagicLan 2
device on the local network.

Supported functions:

 - Authentication
 - Device info
 - Identify
 - Reboot

This code is not in any way associated with or endorsed by Devolo AG. Use at
your own risk.

## Changelog

- 24/12/2020 - Release 0.0.1: Initial release
- 26/04/2021 - Release 0.0.2: Updated to work with firmware 7.10.2.77 (2021-04-01).

## Installation

````
$ pip3 install magiclan2
````

## Basic usage

### Retrieve device info

````
from magiclan import MagicLan2
import json

m = MagicLan2('10.0.0.2')

print(json.dumps(m.info(), indent=4))
````

### Authenticate with a password

````
m = MagicLan2('10.0.0.2', 'YOUR PASSWORD')
````

### Refresh device info

````
m.refresh_info()
print(json.dumps(m.info(), indent=4))
````

### Identify device (blinks the LED)

````
m.identify()
````

### Reboot device

````
m.reboot()
````
