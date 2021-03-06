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

Tested with firmware version 7.8.5.62 (2020-10-02).

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
