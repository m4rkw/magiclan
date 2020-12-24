import requests
import re
import urllib.parse
import json

class MagicLan2:

  def __init__(self, ip, password=None):
    self.ip = ip
    self.r = requests.session()
    self.refresh_info()

    if self.data['AUTHREQUIRED'] == True:
      if not password:
        raise Exception("Password required for MagicLan2 device '%s'" % (self.ip))

      resp = self.post('/', {
        '.PASSWORD': password
      })

      if resp.status_code != 200:
        raise Exception("authentication failed for MagicLan2 device '%s'" % (self.ip))

      self.data = self.parse_info(resp.text)


  def get(self, uri):
    return self.r.get('http://%s%s' % (self.ip, uri))


  def post(self, uri, data):
    urldata = ''

    for key in data:
      if len(urldata) >0:
        urldata += '&'

      urldata += '%s=%s' % (key, urllib.parse.quote_plus(str(data[key])))

    urldata += '&.CSRFTOKEN=%s' % (self.data['CSRFTOKEN'])

    return self.r.post('http://%s%s' % (self.ip, uri),
      data=urldata,
      headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://%s/system' % (self.ip)
      }
    )


  def info(self):
    return self.data


  def refresh_info(self):
    resp = self.get('/assets/data.cfl')

    if resp.status_code != 200:
      raise Exception("failed to communicate with magiclan device at '%s': %s" % (self.ip, resp.text))

    self.data = self.parse_info(resp.text)


  def parse_info(self, info):
    data = {}

    for line in info.rstrip().split("\n"):
      match = re.match('^(.*?)=(.*)$', line)

      if match:
        data[match.group(1)] = match.group(2)

        if data[match.group(1)].isdigit():
          data[match.group(1)] = int(data[match.group(1)])
        elif data[match.group(1)] in ['YES', 'Y']:
          data[match.group(1)] = True
        elif data[match.group(1)] in ['NO', 'N']:
          data[match.group(1)] = False

    return data


  def reboot(self):
    resp = self.post('/', {
      'SYSTEM.GENERAL.HW_RESET': 1
    })

    return resp.status_code == 200


  def identify(self):
    resp = self.post('/', {
      'CONNECTIVITYFB.GENERAL.IDENTIFY_DEVICE': 'YES'
    })

    if resp.status_code != 200:
      raise Exception("failed to identify device '%s': %s" % (self.ip, resp.text))

    self.data = self.parse_info(resp.text)

    return True
